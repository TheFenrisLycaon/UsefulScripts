import sys
import serial


def ListAvailablePorts():
    AvailablePorts = []
    platform = sys.platform
    if platform == "linux":
        for i in range(0, 255):
            try:
                ser = serial.Serial("/dev/ttyUSB" + str(i))
            except serial.serialutil.SerialException:
                pass
            else:
                AvailablePorts.append("/dev/ttyUSB" + str(i))
                ser.close()
    elif platform == "win32":
        for i in range(255):
            try:
                ser = serial.Serial(i, 9600)
            except serial.serialutil.SerialException:
                pass
            else:
                AvailablePorts.append(ser.portstr)
                ser.close()
    else:
        print(
            """This method was developed only for linux and windows
                the current platform isn't recognised"""
        )
    if len(AvailablePorts) == 0:
        print("NO port in use")
        return 0
    else:
        return AvailablePorts
