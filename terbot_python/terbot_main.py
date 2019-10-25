import time, serial, xbox

from roboclaw_3 import Roboclaw

#Windows comport name
# ~ rc = Roboclaw("COM11",115200)
#Linux comport name
rc = Roboclaw("/dev/ttyTHS2", 38400)

rc.Open()
address = 0x80

def move_forward(pwm):
	x = int(pwm*85)   #max 127
	rc.ForwardM1(address,x)
	rc.ForwardM2(address,x)
	time.sleep(0.1)
	
def move_backward(pwm1):
	y = int(abs(pwm1)*85)
	rc.BackwardM1(address,y)
	rc.BackwardM2(address,y)
	time.sleep(0.1)

def move_right(pwm2):
	z = int(pwm2*50)    #max 127
	rc.ForwardM1(address,z)
	rc.BackwardM2(address,z)
	time.sleep(0.1)

def move_left(pwm3):
	w = int(abs(pwm3)*50)    #max 127
	rc.BackwardM1(address,w)
	rc.ForwardM2(address,w)
	time.sleep(0.1)
	
def stop():
	rc.BackwardM1(address,0)	#Stopped
	rc.ForwardM2(address,0)	
	time.sleep(0.1)


joy = xbox.Joystick()

try:
	#xbox
	print("Ready to move with Xbox!!")
	
	while True:
		# ~ move_forward(1)
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
			move_left(pwm3)	
			print("Terbot is turning left!")
			time.sleep(0.1)
		
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
	
		


