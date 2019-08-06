import serial

old = serial.Serial()
old.baudrate = 9600
old.port = 'COM14'

new = serial.Serial()
new.baudrate = 9600
new.port = 'COM11'

while(True):
    if(not old.is_open or not new.is_open):
        try:
            old.open()
            new.open()
        except:
            print("Can't connect to bluetooth")   
            old.close()
            new.close()

    elif(old.inWaiting() and new.inWaiting()):
        old.read()
        new.read()
        old.write(b"c")
        new.write(b"c")

old.close()
new.close()



