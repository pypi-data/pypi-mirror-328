import threading
import errno
import socket
import serial


class Transport (threading.Thread):
    def __init__(self, parent): 
        threading.Thread.__init__(self)
        self.parent = parent
    
    def print(self, message):
        if self.parent:
            print(message)
        else:
            print(message)

    def feedEncodedBytes(self, bytes):

        if self.parent:
            self.parent.service.feed(bytes)



