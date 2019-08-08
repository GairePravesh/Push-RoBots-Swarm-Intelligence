import serial

ser = serial.Serial()
ser.port = "COM11"
ser.baudrate = 9600

ser1 = serial.Serial()
ser1.port = "COM14"
ser1.baudrate = 9600

while(not ser.is_open and not ser1.is_open):
        ser.open()
        ser1.open()

datas = [[b'c', b'f'], [b'f',b'f', b'f']]

ser.write(datas[0].pop(0))
while(datas[0]):
        if(ser.inWaiting()): 
                ser.write(datas[0].pop(0))       

ser.flush()                
ser.write(b't')

while(True):
        if ser.read() == b"1":
                break

ser1.write(datas[1].pop(0))
while(datas[1]):
        if(ser1.inWaiting()):    
                ser1.write(datas[1].pop(0))    
                