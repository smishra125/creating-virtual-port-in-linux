#!/usr/local/bin/python

import sys, time, serial

Port = serial.Serial(port = "/dev/pts/3", baudrate=115200,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
Port.write(b"data is sending\r\n")
# sys.stdout = open('/dev/pts/3', 'w')
# print('hello this is sending data')
time.sleep(0.1)

while(1):

    # Wait until there is data waiting in the serial buffer
    if(Port.in_waiting > 0):

        # Read data out of the buffer until a carraige return / new line is found
        String = Port.readline()

        # Print the contents of the serial data
        print(String.decode('Ascii'))


