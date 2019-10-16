import serial
import xbox,math
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


def move_forward(pwm):
	x = pwm*127    #max 127
	ser.write(("f %d \r" % (abs(x))).encode())
	# ~ ser.write(("f \r").encode())

def move_backward(pwm1):
	y = abs(pwm1)*127
	ser.write(("b %d \r" % (abs(y))).encode())
	# ~ ser.write(("b \r").encode())

def move_right(pwm2):
	z = pwm2*127    #max 127
	ser.write(("r %d \r" % (abs(z))).encode())

def move_left(pwm3):
	w = abs(pwm3)*127    #max 127
	ser.write(("l %d \r" % (abs(w))).encode())	

def stop():
	ser.write(("s \r").encode())


joy = xbox.Joystick()

try:
	#xbox
	print("Ready to move with Xbox!!")
	
	while True:

		if joy.leftY() > 0:
			pwm = joy.leftY()
			move_forward(pwm)
			print("Terbot is moving foward!")	
			time.sleep(0.1)
		
		elif joy.leftY() < 0:
			pwm1 = joy.leftY()
			move_backward(pwm1)	
			print("Terbot is moving backward!")	
			time.sleep(0.1)
		
		elif joy.rightX() > 0:
			pwm2 = joy.rightX()
			move_right(pwm2)	
			print("Terbot is turning right!")
			time.sleep(0.1)
		
		elif joy.rightX() < 0:
			pwm3 = joy.rightX()
			move_right(pwm3)	
			print("Terbot is turning left!")
			time.sleep(0.1)
		
		elif joy.B() == 1:
			stop()
			print("Stop!")
			
		
## Ctrl + c to stop robot
except KeyboardInterrupt:
        # Close serial connection
	stop()    
	#~ file.close() 
	print('\n\n		Stop!!! See you again!')		
	
		
