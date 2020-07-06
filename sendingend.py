#!/usr/local/bin/python
import json
import time, serial

Port = serial.Serial(port = "/dev/pts/1", baudrate=115200,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

##
# We will send the query
# Port.write(b"11 03 006B 0003 7687 \r\n")

with open('/home/shubham/Desktop/modbus_firmwire/queryfile.json') as f:
    data = json.load(f)
print(data)
for key, value in data.items():
    # print(key)
    string = bytes(key + '\r\n', encoding="ascii")
    Port.write(string)
    time.sleep(0.1)

while(1):

    # Wait until there is data waiting in the serial buffer
    if(Port.in_waiting > 0):

        # Read data out of the buffer until a carraige return / new line is found
        String = Port.readline()

        # Print the contents of the serial data
        print(String.decode('Ascii'))


