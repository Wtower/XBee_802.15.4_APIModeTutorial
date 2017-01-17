import XBee

if __name__ == "__main__":
    xbee = XBee.XBee('/dev/ttyUSB0')

    while True:
        Msg = xbee.Receive()
        if Msg:
            # content = Msg[7:-1].decode('ascii')
            # print("Msg: " + content)
            print(Msg)
