#%%
#this code , just for testing dont mind..
from tkinter import *
from tkinter import ttk
import pyfirmata

port = input ("Select Correct Port: COM")
comport= "COM" + port
board = pyfirmata.Arduino(comport)

root = Tk()
root.title("Firmta Arduino Controller!")
root.resizable(600, 600)
led = board.get_pin('d:9:o')

def On():
    led.write(1)
def off():
    led.write(0)

ttk.Button(root, text="LED ON", width="11", command=On).grid(row=1, column=0, ipadx= 1, ipady= 1)
ttk.Button(root, text="LED OFF", width="11", command=off).grid(row=1, column=1, ipadx= 1, ipady= 1)
root.mainloop()

#code(1) ends here
# %%
def rfid():
    import serial
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = 'COM3'
    
    #this columns specifically takes the data from my arduino's rfid and tansform into seperate digital codes for every 
    #this code is suppose to be added in the tkinter
    ser.open()
    RFID_Data=ser.readline() 
    if RFID_Data:
        RFID_Data = RFID_Data.decode()  #Decode arduino Serial
        RFID_Data = RFID_Data.strip()   #Strip Arduino Data to remove string
        RFID_Data=int(RFID_Data)       #data value ko integer form me karne ke liye
        return(RFID_Data)
    

            
#this loop for continuous reading of attendance
while(True):
    data = rfid() 
    print(data)
    print("Attendance Registered")

#%%
#import libraries
print("----ATTENDANCE SYSTEM----")
import tkinter as tk
from tkinter import *
import time



#initialize window
window = tk.Tk()
window.title("Attendance System")
window.geometry("400x400")

#serial port and baud rate
#baud rate defined is a rate at which a serial port transititions signal from pc to my arduino
#9600 baud rate could be defined as 9600b/pm
def rfid():
    import serial
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = 'COM3'
    
    #this columns specifically takes the data from my arduino's rfid and tansform into seperate digital codes for every 
    #this code is suppose to be added in the tkinter
    ser.open()
    RFID_Data=ser.readline() 
    if RFID_Data:
        RFID_Data = RFID_Data.decode()  #Decode arduino Serial
        RFID_Data = RFID_Data.strip()   #Strip Arduino Data to remove string
        RFID_Data=int(RFID_Data)       #data value ko integer form me karne ke liye
        return(RFID_Data)
    
    
            
#this loop for continuous reading of attendance
 

def countdown (t):
    while t:
        mins,secs=divmod(t,60)
        timer="{:02d}:{:02d}".format(mins,secs)
        print(timer,end="\r")
        time.sleep(1)
        t-=1

    
#11011913495

attendance = []

# Taking Attendance at the beginning of the class
print("Please input your attendance at the beginning of the class ")
data = rfid()
countdown(5)


print("Please input your attendance in the middle of the class")
data = rfid()
countdown(5)

# Taking Attendance at the end of the class

print("Please input your attendance at the end of the class")
data = rfid()

# rfidnum = [11011913495,124]
# name=['Samyak','name2']
# for i in range(len(name)):
#     if rfidnum[i]==data:
#         print("{}'s attendance is recorded".format(name[i]))
#     else:
#         pass

dict={11011913495:'samyak gupta e22ce',1424410095:'Arpit Panwar',78897795:'Rajul Gupta',22222310495:'Khyati Satija'}
x=dict.get(data)
print("{}'s attendance is recorded".format(x))

# Taking Attendance thrice after the student has inputted attendance

# Outputting the Attendance
print("Attendance:", attendance)


#button to call ReadData function
#while loop would be inserted


#main window loop
# %%
