#!/usr/local/bin/python

import serial, sys, time

serialPort = serial.Serial(port = "/dev/pts/2", baudrate=115200,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

while(1):

    # Wait until there is data waiting in the serial buffer
    if(serialPort.in_waiting > 0):

        # Read data out of the buffer until a carraige return / new line is found
        serialString = serialPort.readline()

        # Print the contents of the serial data
        print(serialString.decode('Ascii'))

        # Tell the device connected over the serial port that we recevied the data!
        # The b at the beginning is used to indicate bytes!
        serialPort.write(b"Thank you for sending data \r\n")
        time.sleep(1)

        serialPort.flushOutput()



#####################################################################################################3
# ser = serial.Serial('/dev/pts/7', 9600)
# print(ser)

# with open('/home/shubham/Desktop/modbus_firmwire/queryfile.json') as f:
#     data = json.load(f)
# print(data)
#
# # d  = data.get('11 03 006B 0003 7687')
# # print(d)
#
# for key, value in data.items():
#     print(value)