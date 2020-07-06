#!/usr/local/bin/python
import json
import serial, sys, time

serialPort = serial.Serial(port = "/dev/pts/2", baudrate=115200,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
while(1):

    # Wait until there is data waiting in the serial buffer
    if( serialPort.in_waiting > 0 ):

        # Read data out of the buffer until a carraige return / new line is found
        serialString = serialPort.readline()

        # Print the contents of the serial data
      #  str = serialString.decode('Ascii')
        str = serialString.decode('UTF-8')
        print(str)

        # Tell the device connected over the serial port that we recevied the data!
        # The b at the beginning is used to indicate bytes!
        with open('/home/shubham/Desktop/modbus_firmwire/queryfile.json') as f:
            data = json.load(f)
        for key, value in data.items():
            # pass
            # print(value)
            if key == str[0:-2]:
                string = bytes(value+'\r\n', encoding="ascii")
                serialPort.write(string)
                print("Data send")
                time.sleep(0.1)
                serialPort.flushOutput()



