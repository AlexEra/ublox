import serial
import ublox.ubx as ubx
from time import sleep


if __name__ == '__main__':
    x = ubx.UbxStream(serial.Serial(port='COM29', baudrate=115200, timeout=1))
    # x.enable_message
    while True:
        msg = x.read()
        try: 
            print(f'iTOW: {msg.iTOW}, lon: {msg.lon}, lat: {msg.lat}, height: {msg.height}, hMSL: {msg.hMSL}, hAcc: {msg.hAcc}, vAcc: {msg.vAcc}')
        except Exception as e:
            pass
        sleep(0.2)
        # self.iTOW, self.lon, self.lat, self.height, self.hMSL, self.hAcc, self.vAcc = struct.unpack('=LllllLL', payload_cpy)


