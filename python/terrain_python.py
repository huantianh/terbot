import serial
import math
import xbox
import time

# Serial setup, this lets you plug the arduino into any USB port on the raspi
i = 0
portname = '/dev/ttyACM'
while True:
	try:
	        ser = serial.Serial(portname + str(i), 115200, timeout=1)
	        ser.flushInput()
	        ser.flushOutput()
	        break
	except:
		i += 1

ser.reset_input_buffer()
ser.reset_output_buffer()


def move_forward():
	ser.write(("f \r").encode())

def move_backward():
	ser.write(("b \r").encode())

def move_left():
	ser.write(("l \r").encode())

def move_right():
	ser.write(("r \r").encode())

def stop():
	ser.write(("s \r").encode())

#xbox
joy = xbox.Joystick()
while True:
	
	if (joy.Y()):
		move_forward()
		print("Terbot is moving foward!")	
	elif (joy.A()):
		move_backward()	
		print("Terbot is moving backward!")	
	elif (joy.X()):
		move_left()	
		print("Terbot is turning left!")
	elif (joy.B()):
		move_right()
		print("Terbot is turning right!")
	elif (joy.Start()):
		stop()
		print("Stop!")
