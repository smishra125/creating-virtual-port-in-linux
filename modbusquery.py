import simplejson as json
import time, serial

Port = serial.Serial(port = "/dev/pts/1", baudrate=115200,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

def get_modbus_crc( data ):
    crc = 0xFFFF
    for pos in data:
        crc ^= pos					# Bitwise XOR
        for i in range(8):
            if ((crc & 1) != 0):
                crc >>= 1
                crc ^= 0xA001
            else:
                crc >>= 1

    crcs = "%04X" % (crc)
    crcs = crcs[2:] + crcs[0:2]
    return crcs

try:
    with open('/home/shubham/Desktop/RTUdatalogger/modbus_config/WST_RTD_RS485.json', 'r') as f:
        data = json.load(f)
    # print(data)

except Exception as e:
    print('Error reading Firmware version: %s', e)

query_params = data.get('query_params')
print(query_params)
for element in query_params:
    function_id = element['function_id']
    start_register = element['start_register']
    register_count = element['register_count']

modbus_data = data.get('data')
for element in modbus_data:
    # print(element)
    params = element['params']
    for param in params:
        print(param)
        name = ['name']
slaveId = 33
slaveIdHex = "%02X" % slaveId
funIdHex = "%02X" % function_id
startRegHex = "%04X" % start_register
regCountHex = "%04X" % register_count
message = slaveIdHex + funIdHex + startRegHex + regCountHex
crc = get_modbus_crc( bytearray.fromhex( message ) )
message = message+crc
print("sendind: "+message)

string = bytes(message + '\r\n', encoding="UTF-8")
Port.write(string)
time.sleep(0.1)

while(1):

    # Wait until there is data waiting in the serial buffer
    if(Port.in_waiting > 0):

        # Read data out of the buffer until a carraige return / new line is found
        String = Port.readline()

        # Print the contents of the serial data
        print("Recieved: "+String.decode('UTF-8'))
        # a = String.decode('UTF-8')
        # print("Recieved: " + a[2:])