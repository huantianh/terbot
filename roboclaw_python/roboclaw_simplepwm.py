import time, serial, xbox

from roboclaw_3 import Roboclaw

#Windows comport name
# ~ rc = Roboclaw("COM11",115200)
#Linux comport name
rc = Roboclaw("/dev/ttyTHS2", 38400)

rc.Open()
address = 0x80

def move_forward(pwm):
	x = pwm*70   #max 127
	rc.ForwardM1(address,pwm)
	rc.ForwardM2(address,pwm)
	time.sleep(0.1)
	
def move_backward(pwm1):
	y = abs(pwm1)*70
	rc.BackwardM1(address,pwm1)
	rc.BackwardM2(address,pwm1)
	time.sleep(0.1)

def move_right(pwm2):
	z = pwm2*50    #max 127
	rc.ForwardM1(address,pwm2)
	rc.BackwardM2(address,pwm2)
	time.sleep(0.1)

def move_left(pwm3):
	w = abs(pwm3)*50    #max 127
	rc.BackwardM1(address,pwm3)
	rc.ForwardM2(address,pwm3)
	time.sleep(0.1)
	
def stop():
	rc.BackwardM1(address,0)	#Stopped
	rc.ForwardM2(address,0)	
	time.sleep(0.1)


joy = xbox.Joystick()


while(1):
	rc.ForwardM1(address,32)	#1/4 power forward
	rc.BackwardM2(address,32)	#1/4 power backward
	time.sleep(2)
	
	rc.BackwardM1(address,32)	#1/4 power backward
	rc.ForwardM2(address,32)	#1/4 power forward
	time.sleep(2)

	rc.BackwardM1(address,0)	#Stopped
	rc.ForwardM2(address,0)		#Stopped
	time.sleep(2)

	m1duty = 16
	m2duty = -16
	rc.ForwardBackwardM1(address,64+m1duty)	#1/4 power forward
	rc.ForwardBackwardM2(address,64+m2duty)	#1/4 power backward
	time.sleep(2)
	
	m1duty = -16
	m2duty = 16
	rc.ForwardBackwardM1(address,64+m1duty)	#1/4 power backward
	rc.ForwardBackwardM2(address,64+m2duty)	#1/4 power forward
	time.sleep(2)

	rc.ForwardBackwardM1(address,64)	#Stopped
	rc.ForwardBackwardM2(address,64)	#Stopped
	time.sleep(2)
	
