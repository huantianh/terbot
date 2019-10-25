import serial
import xbox,math
import time

# Serial setup, this lets you plug the arduino into any USB port on the raspi
i = 0
portname = '/dev/ttyACM'
while True:
	try:
		ser = serial.Serial(portname + str(i), 38400, timeout=1)
		ser.flushInput()
		ser.flushOutput()
		break
	except:
		i += 1

ser.reset_input_buffer()
ser.reset_output_buffer()


def move_forward(pwm):
	x = pwm*70   #max 127
	ser.write(("f %d \r" % (abs(x))).encode())
	time.sleep(0.1)
	
	

def move_backward(pwm1):
	y = abs(pwm1)*70
	ser.write(("b %d \r" % (abs(y))).encode())
	time.sleep(0.1)


def move_right(pwm2):
	z = pwm2*50    #max 127
	ser.write(("r %d \r" % (abs(z))).encode())
	time.sleep(0.1)

def move_left(pwm3):
	w = abs(pwm3)*50    #max 127
	ser.write(("l %d \r" % (abs(w))).encode())	
	time.sleep(0.1)

def stop():
	ser.write(("s \r").encode())
	time.sleep(0.1)


joy = xbox.Joystick()

try:
	#xbox
	print("Ready to move with Xbox!!")
	
	while True:

		if joy.leftY() > 0:
			pwm = joy.leftY()
			move_forward(50)
			print("Terbot is moving foward!")	
			time.sleep(0.1)
		
		elif joy.leftY() < 0:
			pwm1 = joy.leftY()
			move_backward(50)	
			print("Terbot is moving backward!")	
			time.sleep(0.1)
		
		elif joy.rightX() > 0:
			pwm2 = joy.rightX()
			move_right(50)	
			print("Terbot is turning right!")
			time.sleep(0.2)
		
		elif joy.rightX() < 0:
			pwm3 = joy.rightX()
			move_left(50)	
			print("Terbot is turning left!")
			time.sleep(0.2)
		
		elif joy.B() == 1:
			stop()
			print("Stop!")
			time.sleep(0.1)
			
		
## Ctrl + c to stop robot
except KeyboardInterrupt:
        # Close serial connection
	stop()    
	#~ file.close() 
	print('\n\n		Stop!!! See you again!')		
	
		
