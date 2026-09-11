#Yousef E FOR ONLY ONE LEG AS OF 9/10/26
#Yousef E FOR ONLY ONE LEG AS OF 9/10/26
#Yousef E FOR ONLY ONE LEG AS OF 9/10/26

import math
import time
from adafruit_servokit import ServoKit #was programmed on the RPi where it has the libraries installed
kit = ServoKit(channels=16) 

euler = 2.7183

def move_servo(channel, angle):
    kit.servo[channel].angle = angle

def angleCalc(x, y):
    angle = math.degrees(math.atan(x/y)) 
    c = math.sqrt(x**2 + y**2)
    Bangle = math.degrees(math.acos((a**2 + c**2 - b**2)/(2*a*c)))
    Cangle = math.degrees(math.acos((a**2+b**2-c**2)/(2*a*b)))
    offsetFunction = float(181.9*(euler)**(-0.2929*c))
    move_servo(13, 180-Cangle) #default
    move_servo(12, Bangle-offsetFunction-angle) #default
    time.sleep(delay)

move_servo(14, 115) #default configuration
move_servo(13, 90) #default configuration
move_servo(12, 52) #default configuration

a = 10
b = 13

x = -5 #int(input("input x coordinate in cm: "))#-10
y = -14#int(input("input y coordinate in cm: "))#-15

time.sleep(3)

delay=0.2

for z in range(0,20): # draw rectangle 10 times
    x += 5;
    angleCalc(x, y)
    
    y += 8;
    angleCalc(x, y)
    
    x -= 5;
    angleCalc(x, y)
    
    y -= 8;
    angleCalc(x, y)
