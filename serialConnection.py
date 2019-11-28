import serial
import serial.tools.list_ports

#print(list(serial.tools.list_ports.comports()).__getitem__(1))

def getComPort():
    i = 0;
    while(True):
        try:
            list(serial.tools.list_ports.comports()).__getitem__(i)
            myCom = list(serial.tools.list_ports.comports()).__getitem__(i)[0]
            if list(serial.tools.list_ports.comports()).__getitem__(i)[1] == 'JLink CDC UART Port ('+myCom+')':
                return myCom
            i+=1
        except:
            break
    return None

print(getComPort())

# LED Test that Works

# import serial, time, struct
#
# ser = serial.Serial(port = 'COM8',baudrate=115200)
# strToString = ""
#
# if ser.is_open:
#     print("open")
#
# output = bytearray([10,1,0,1])
# print(output)
# x=0
# while x< 10000:
#     x+=1
#     ser.write(output)
#
# ser.close()
