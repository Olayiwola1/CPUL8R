import serial
import serial.tools.list_ports
from gets import *

#print(list(serial.tools.list_ports.comports()).__getitem__(1))

# Create Function to detect the com port on the computer
def getComPort():
    i = 0;
    while(True):
        try:
            list(serial.tools.list_ports.comports()).__getitem__(i)
            myCom = list(serial.tools.list_ports.comports()).__getitem__(i)[0]
            #ensure that the comport that was detected was for the pacemaker device
            if list(serial.tools.list_ports.comports()).__getitem__(i)[1] == 'JLink CDC UART Port ('+myCom+')':
                return myCom    #return comport name if found
            i+=1
        except:
            break
    return False    #return False if no comport found (i.e. device not connected)

def sendValues(comport):
    ser = serial.Serial(port=comport, baudrate=115200)
    output = bytearray([])
    usr = getRecent()

    modes = {'aoo':[1,3,0], 'voo':[2,3,0], 'aai':[1,1,0], 'vvi':[2,2,0], 'doo':[0,3,0], 'aoor':[1,3,1], 'voor':[2,3,1], 'aair':[1,1,1], 'vvir':[2,2,1], 'door':[0,3,1]}

    output.append(modes[getValue(usr, 'mode')][0])
    output.append(modes[getValue(usr, 'mode')][1])
    output.append(modes[getValue(usr, 'mode')][2])
    output.append(round(getValue(usr, 'lower')))
    output.append(round(getValue(usr, 'upper')))
    output.append(round(getValue(usr, 'AAmp')*10))
    output.append(round(getValue(usr, 'VAmp')*10))
    output.append(round(getValue(usr, 'APW')*100))
    output.append(round(getValue(usr, 'VPW')*100))

    arp = round(getValue(usr, 'ARP'))
    output.append(arp//10)
    output.append(arp%10)
    vrp = round(getValue(usr, 'VRP'))
    output.append(vrp//10)
    output.append(vrp%10)

    output.append(round(getValue(usr, 'MSR')))
    output.append(round(getValue(usr, 'FAVD')-70))

    thresholds = {'V-Low':1, 'Low':2, 'Med-Low':3, 'Med':4, 'Med-High':5, 'High':6, 'V-High':7}

    output.append(thresholds[getValue(usr, 'AT')])
    output.append(round(getValue(usr, 'ReactTime')))
    output.append(round(getValue(usr, 'RF')))
    output.append(round(getValue(usr, 'RecoveryTime')))

    print(output)
    for i in range(len(output)):
        print(output[i])

    x=0
    while x< 5000:
        x+=1
        ser.write(output)
    ser.close()

# LED Test that Works
#
# import serial, time, struct
#
# ser = serial.Serial(port = 'COM8',baudrate=115200)
#
# if ser.is_open:
#     print("open")
#
# output = bytearray([10,0,0,1])
# print(output)
# x=0
# while x< 10000:
#     x+=1
#     ser.write(output)
#
# ser.close()
