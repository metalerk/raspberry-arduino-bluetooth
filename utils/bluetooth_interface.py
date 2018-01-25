import bluetooth
import time

class BluetoothController:
    def __init__(self, mac_address, port):
        self.sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
        self.sock.connect((mac_address, port))

    def on(self):
        self.sock.send('w')

    def off(self):
        self.sock.send('s')

    def __del__(self):
        self.sock.close()
