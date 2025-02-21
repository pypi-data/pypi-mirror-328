import argparse

from phycat.protocol.phycatService import *

from polypacket.polyservice import PolyService, PolyPacket

from phycat.interfaces.PhycatInterface import PhycatInterfaceDriver

from cliify import commandParser, command

from phycat.interfaces import *
from phycat.helpers.driver_helper import load_driver_class
import yaml
from importlib import resources
import os
import logging
from functools import partial

log = logging.getLogger(__name__)


class SystemInfo:
    def __init__(self):
        self.name = ""
        self.portCount = 0
        self.interfaceCount = 0
        self.clockSpeed = 0


class DiscoveryState:
    def __init__(self):
        self.state = None
        self.index = 0

@commandParser(subparsers=['interfaces'], allow_eval=True)
class PhycatSession:
    def __init__(self, connString = None, server_config = None): 
        """
            Create a new PhycatSession object.

            connString: connection string to use to connect to the Phycat device.

            server_config: Configuration if running as server (i.e. acting as the Phycat device)
        
        """

        pkg_dir = resources.files('phycat')
        protocol_file = os.path.join(pkg_dir, 'protocol', 'poly', 'phycat.yml')


        self.service = PolyService(protocol_file)
        self.service.silenceAll = True
        self.service.addHandler('default', self._handleMessage)
        #self.service.addHandler()


        self.portLabels: dict = {}
        self.interfaces: dict[ str, PhycatInterfaceDriver ] = {}


        #Default handlers for messages
        self.message_handler = self.handleMessage
        self.discovery_complete_handler = self.handleDiscoveryComplete

        #Track state of session
        self.system = SystemInfo()
        self.discoState = DiscoveryState()


        #Server mode
        self.server_mode = False
        if server_config:
            self.serve(server_config)

    @command(completions={'path': ['$nodes','!help']})
    def help(self,path: str):
        strHelp = self.getHelp(path)

    @command
    def connect(self, connString: str):
        """
            Connect to a Phycat device using the specified connection string.

            Connection strings are of the form:

            serial:/dev/ttyS0:115200-8N1
            tcp:8020 (listen on port 8020)
            tcp:localhost:8020 (connect to localhost on port 8020)

        """
        self.service.connect(connString)
        self.discover()
        # if self.client.connected:
        #     self.startDiscovery()

    def close(self):
        self.service.close()
        

    @command()
    def test(self):
        print("Test command")
        log.error("Test error")
        log.info("Test info")
        log.debug("Test debug")

    @command(completions={'path': ['$nodes']})
    def ls(self, path = '/'):
        
        if path == '/':
            print(f"{self.interfaces.keys()}")
        

    @command( completions= {'config': lambda self: os.listdir(os.path.join(resources.files('phycat'),'configs')) + ['$file']})
    def serve(self, config):


        if( not os.path.exists(config) ):
            #check for default configs in the phycat package
            default_config_dir = os.path.join(resources.files('phycat'),'configs')
            if not config.endswith('.yml'):
                config = config + '.yml'
            
            if os.path.exists( os.path.join(default_config_dir,  config) ):
                config = os.path.join(default_config_dir, config)
            else:
                print(f"Could not find server config {config}")
                return

        self.server_mode = True
        with open(config, 'r') as file:
            config = yaml.load(file, Loader=yaml.FullLoader)
        
            self.portLabels = {} 
            if 'ports' in config:
                for handle, label in config['ports'].items():
                    self.portLabels[int(handle)] = str(label) 
            
            if 'interfaces' in config:
                for name, iface_config in config['interfaces'].items():
                    handle = self.getIfaceHandle(name)
                    iface = load_driver_class(iface_config['driver'])(self,handle, iface_config)
                    self.interfaces[name] = iface
                
        txt = yaml.dump(config)
        print(f"Loaded server config:\n{txt}")

    @command
    def discover(self):
        self.startDiscovery()    

    def startDiscovery(self):
        self.discovery_mode = 'port_labels'
        self.sendRequest(requestType.SYSTEM)
        self.discoState.state = 'system'
        self.discoState.index = 0

    def sendRequest(self, type, handle = None, index = None):

        packet = Request()
        packet.requestType = type

        if handle is not None:
            packet.handle = handle
        
        if index is not None:
            packet.index = index

        self.send(packet)


    def print(self, message):
        print(message)

    def getIfaceLabel(self, handle):

        ifaceType = handleType(handle >> 16).name.lower()

        if ifaceType == "gpio":
            pinLabel = self.getPinLabel(handle)
            return f"{ifaceType}{pinLabel}"
        else:

            ifaceNum = handle & 0xFFFF
            return f"{ifaceType}{ifaceNum}"

    def getIfaceHandle(self, label):

        try:

            if label in self.interfaces:
                return self.interfaces[label].handle
            else:
                if label.startswith("gpio"):
                    pinHandle = self.getPinHandle(label[4:])
                    return handleType.GPIO.value << 16 | pinHandle
                elif label.startswith("i2c"):
                    return handleType.I2C.value << 16 | int(label[3:])
                elif label.startswith("uart"):
                    return handleType.UART.value << 16 | int(label[4:])
                else:
                    #TODO support more interfaces
                    print(f"Invalid interface label {label}")
                    return None
        
        except:
            print(f"Invalid interface label {label}")
            return None
    
    
    def getPinHandle(self, label):
        """ Converts a pin label to a uint32 handle.

        example: 

            portLabels = { 0x01: "GPIOA", 0x02: "GPIOB" }

            getPinHandleFromLabel("GPIOA4") -> 0x00010004
        
        """

        port = None 
        pin = None

        for handle, lbl in self.portLabels.items():
            if label.startswith(lbl):
                port = handle
                pin = int(label[len(lbl):])

                return port << 8 | (pin & 0xFF)
                break
                
        return None
    
    def getPinLabel(self, handle):
        port = (handle >> 8) & 0xFF
        pin = handle & 0xFF

        return self.portLabels[port] + str(pin)
    


    def send(self, msg : BasePacket | PolyPacket, fields = {} ):

        #print(f"---> {msg.__dict__}")
        self.service.sendPacket(msg, fields)


    def addInterface(self, iface: PhycatInterfaceDriver):

        if iface.name in self.interfaces:
            print(f"Interface {iface.name} already exists")
            return
        else:
            self.interfaces[iface.name] = iface

    

    def _handleMessage(self, service, ppPacket : PolyPacket, resp: BasePacket):

        self.message_handler(service, ppPacket , resp)
            

    
    def handleMessage(self, service, ppPacket : PolyPacket, resp: BasePacket):

        type = ppPacket.typeId 
        packetType = ppPacket.desc.name.lower()
        req : BasePacket = ppPacket.toBasePacket()
        #print(f"Received message {ppPacket.toJSON()}")


        if packetType == "port":
            self.portLabels[self.discoState.index] = req.label
            self.discoState.index += 1
            if self.discoState.index < self.system.portCount:
                self.sendRequest(requestType.PORT, index=self.discoState.index)
            else:
                self.discoState.state = 'interfaces'
                self.discoState.index = 0
                self.sendRequest(requestType.CAPABILITIES, index=0)
            
            return
        elif packetType == "system":
            self.system.name = req.label
            self.system.portCount = req.portCount
            self.system.interfaceCount = req.interfaceCount
            self.system.clockSpeed = req.clockSpeed

            self.discoState.state = 'ports'
            self.discoState.index = 0
            self.sendRequest(requestType.PORT, index=0)

            return


        elif packetType.endswith('capabilities'):
            hType = req.handle >> 16


            if hType == handleType.UART:
                iface = UartInterface(self, req.handle, req)
                self.addInterface(iface)
            elif hType == handleType.I2C:
                iface = I2cInterface(self, req.handle, req)
                self.addInterface(iface)
            

            self.discoState.index += 1
            if self.discoState.index < self.system.interfaceCount:
                self.sendRequest(requestType.CAPABILITIES, index=self.discoState.index)
            else:
                self.discoState.state = None
                self.discoState.index = 0
                self.discovery_complete_handler()
            


        
        
        
        pass


    def handlePortLabel(self, msg):
        
        self.portLabels[msg.handle] = msg.label

    def handleDiscoveryComplete(self):

        info = "Discovery complete\n"
        info += "Port labels:\n"

        for handle, label in self.portLabels.items():
            info += f"  {label}: {handle}\n"

        info += "Interfaces:\n"
        for name, iface in self.interfaces.items():
            info += f"  {name}\n"

        print(info)



    