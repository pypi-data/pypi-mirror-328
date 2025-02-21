from phycat.interfaces.PhycatInterface import PhycatInterfaceDriver
from phycat.protocol.phycatService import *
from cliify import commandParser, command
from phycat.interfaces.PtyTap import PTYTap

class PTYTap:
    def __init__(self, interface):
        #TODO complete this class
        pass




class UartInterface(PhycatInterfaceDriver):
    def __init__(self, session, handle, capabilities=None):
        super().__init__(session, handle)
        self.capabilities = capabilities
        self.config = None
        self.pty = None
    
    def configure(self, config):
        self.config = config
        self.send(config)

    @command
    def write(self, data):
        msg = UartData()
        msg.handle = self.handle
        msg.data = data
        self.send(msg)

    @command(completions={'name': ['$file']})
    def tap(self, name):
        """Open a PTY tap at the specified path"""
        if self.pty:
            print("PTY tap already exists. Close it first.")
            return False
        
        self.pty = PTYTap(self)
        if not self.pty.start(name):
            self.pty = None
            return False
        return True

    def close_tap(self):
        """Close the PTY tap if it exists"""
        if self.pty:
            self.pty.stop()
            self.pty = None

    def handle_data(self, uartData: UartData):
        print(f"{self.name} <-- {uartData.data}")
        
        if self.pty:
            self.pty.write(uartData.data)
    

