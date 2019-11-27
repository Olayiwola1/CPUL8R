#import serial, time

# ser = serial.Serial(port = 'COM8', baudrate = 115200, timeout=1)
#
#
#
# print(ser.is_open)
# ser.close()
# print(ser.is_open)

import serial, time, struct

ser = serial.Serial(port = 'COM8', baudrate = 9600, timeout=1)
strToString = ""


i = float(input("What number? "))
strToString += str(struct.pack("d", i))
print(strToString)
# strToString = str.encode(strToString)
strToString = strToString.encode()
print(strToString)
print(ser.name)
ser.write(strToString)
ser.close()



# import serial, time, struct
#
# ser = serial.Serial(port = 'COM8', baudrate = 9600, timeout=1)
#
# if __name__ == '__main__':
#     strToString = ""
#
#     for x in range(4):
#         i = input("What number? ")
#         strToString += struct.pack("!B", i)
#
#     while(true):
#         print(ser.name)
#         ser.write(strToString)
#
#     ser.close()
