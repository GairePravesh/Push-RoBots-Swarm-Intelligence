from tkinter import *
import controller
import serial
import directions

root = Tk()
root.title("Controller")
root.geometry("500x600") 
root.resizable(0, 0)

canva = Canvas(root, width=500, height=600, bg="white")
canva.pack()

L1 = Label(canva, text="Source")
L1.place(x=50, y=10)

E1 = Entry(canva, bd =5)
E1.place(x=50, y=30)

L2 = Label(canva, text="Destination")
L2.place(x=350, y=10)
E2 = Entry(canva, bd =5)
E2.place(x=350, y=30)

L = Label(canva, text="INPUTS").place(x=245, y = 50)

L3 = Label(canva, text="Robo1")
L3.place(x=50, y=60)
E3 = Entry(canva, bd =5)
E3.place(x=50, y=80)

L4 = Label(canva, text="Robo2")
L4.place(x=350, y=60)
E4 = Entry(canva, bd =5)
E4.place(x=350, y=80)

datas = []
paths = []
direcs = []

conversionData = {(0,0):0,(0,1):1,(0,2):2,(1,0):3,(1,1):4,(1,2):5,(2,0):6,(2,1):7,(2,2):8,(3,0):9,(3,1):10,(3,2):11,}
nodePos = [(150,130),(250,130),(350,130),(150,230),(250,230),(350,230),(150,330),(250,330),(350,330),(150,430),(250,430),(350,430),]

def joinLines(s,e, col, diff):
    canva.create_line(nodePos[conversionData[s]][0] + diff,nodePos[conversionData[s]][1] + diff,nodePos[conversionData[e]][0] + diff,nodePos[conversionData[e]][1] + diff,fill = col, width=5)

def joinGrids():
    canva.create_line(nodePos[0],nodePos[1])
    canva.create_line(nodePos[0],nodePos[3])
    canva.create_line(nodePos[1],nodePos[2])
    canva.create_line(nodePos[4],nodePos[1])
    canva.create_line(nodePos[4],nodePos[7])
    canva.create_line(nodePos[2],nodePos[5])
    canva.create_line(nodePos[3],nodePos[4])
    canva.create_line(nodePos[3],nodePos[6])
    canva.create_line(nodePos[5],nodePos[4])
    canva.create_line(nodePos[8],nodePos[5])
    canva.create_line(nodePos[7],nodePos[6])
    canva.create_line(nodePos[6],nodePos[9])
    canva.create_line(nodePos[8],nodePos[7])
    canva.create_line(nodePos[7],nodePos[10])
    canva.create_line(nodePos[8],nodePos[11])
    canva.create_line(nodePos[9],nodePos[10])
    canva.create_line(nodePos[10],nodePos[11])


def submit():
    global datas
    datas = [E1.get(), E2.get(), E3.get(), E4.get()]
    E1.delete(0, END)
    E2.delete(0, END)
    E3.delete(0, END)
    E4.delete(0, END)

def src_dest(col="red"):
        global direcs
        paths, direcs = controller.init(datas)
        try:
                for i in range(len(paths[2])-1):
                        joinLines(paths[2][i],paths[2][i+1],col, 10)
        except:
                for i in range(len(paths[1])-1):
                        joinLines(paths[1][i],paths[1][i+1],col, 10)

def robo1(col="green"):
        try:
                paths, direcs = controller.init(datas)    
                for i in range(len(paths[0])-1):
                        joinLines(paths[0][i],paths[0][i+1],col, 0)
        except:
                pass
def robo2(col="blue"):
        paths, direcs = controller.init(datas)  
        for i in range(len(paths[1])-1):
                joinLines(paths[1][i],paths[1][i+1],col, -10)

def clear():
    src_dest('white')
    robo1('white')
    robo2('white')
    joinGrids()

def serialCommunications():
        global direcs

        r1Data = list(direcs[0].split(' '))
        r2Data = list(direcs[1].split(' '))
        ser = serial.Serial()
        ser.baudrate = 9600
        ser.port = 'COM11'
        
        ser1  = serial.Serial()
        ser1.baudrate = 9600
        ser1.port = "COM14"

        datas = [r1Data, r2Data]
       
        while(not ser.is_open and not ser1.is_open):
                ser.open()
                ser1.open()
                ser.write((r1Data.pop(0)).encode())
                while(datas[0]):
                        if(ser.inWaiting()): 
                                ser.write((r1Data.pop(0)).encode())
                ser.flush()                
                ser.write(b't')

                while(True):
                        if ser.read() == b"1":
                                break

                ser1.write((r2Data.pop(0)).encode())
                while(datas[1]):
                        if(ser1.inWaiting()):    
                                ser1.write((r2Data.pop(0)).encode())
                                
                

Button(canva, text="Submit", width=10, command = submit).place(x=220, y=80)
Button(canva, text="Src to Dest", width=10, command = src_dest).place(x=200, y=500)
Button(canva, text="Robo1 Path", width=10, command = robo1).place(x=100, y=500)
Button(canva, text="Robo2 Path", width=10, command = robo2).place(x=300, y=500)
Button(canva, text="clear", width=10, command = clear).place(x=100, y=550)
Button(canva, text="Connect to Robots", width=15, command = serialCommunications).place(x=300, y=550)
count = 0
x=125
y=125
for idx in range(12):
    count += 1
    button = Button(canva, text=idx, width=5)
    button.place(x=x, y=y)
    x += 100
    if count == 3:
        count = 0 
        y+=100
        x = 125
joinGrids()
root.mainloop()