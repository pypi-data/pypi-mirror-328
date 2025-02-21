
from .EmulatedMemory import EmulatedMemory
from cliify import commandParser, command
from phycat.protocol.phycatService import *
from polypacket.polyservice import PolyPacket 

@commandParser(subparsers=['devices'])
class PhycatInterfaceDriver:
    def __init__(self, session, handle ):
        self.handle = handle
        self.name = session.getIfaceLabel(self.handle)
        self.type = None
        self.label = None 
        self.session  = session
        self.devices : list[PhycatDevice] = []
        self.pinLabels = {}

    def addDevice(self, device):
        device.interface = self
        self.devices.append(device)

    def send(self, msg):
        msg.handle = self.handle
        self.session.send(msg)
        pass

    def getPinLabel(self, handle):
        self.session.getPinLabel(handle)
    
    def getPinHandle(self, label):
        self.session.getPinHandle(label)

    def handleMessage(self, msg : PolyPacket):
        print(f"Message handler not implemented for {self.name}")
        pass

    def getCapabilities(self) -> PolyPacket:
        pass


class PhycatDevice: 
    def __init__(self, emulated = False):
        self.memory = EmulatedMemory()
        self.emulated = emulated
        self.interface = None


    def write(self, address, data):
        self.memory.write(address, data)

    
        