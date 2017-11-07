import time
import pigpio

# Setup GPIO
servo_0 = 20
servo_1 = 21

servo0_trim = -100

dira = 23
pwma = 18
 
dirb = 24
pwmb = 25

FWD = 1
BWD = 0

rMotor = 0
lMotor = 0
RM = 0
LM = 0



pi = pigpio.pi()
 
pi.set_mode(dira, pigpio.OUTPUT)
pi.set_mode(pwma, pigpio.OUTPUT)

pi.set_mode(dirb, pigpio.OUTPUT)
pi.set_mode(pwmb, pigpio.OUTPUT)
 

pi.write(dira, 0)
pi.write(dirb, 0)
pi.set_PWM_frequency(pwma, 100)
pi.set_PWM_frequency(pwmb, 100)

pi.set_mode(servo_0, pigpio.OUTPUT)
pi.set_mode(servo_1, pigpio.OUTPUT)

print("Sideboard loaded")

def servo0(pos0):
    if pos0 >= 0:
        print (pos0)
        pos0 = ((pos0 * 11.1) + 1500 + servo0_trim)
        print (pos0)
        pi.set_servo_pulsewidth(servo_0, pos0)
    
    elif pos0 < 0:
        print ("neg")
        print (pos0)
        pos0 = (servo0_trim + 1500 - (abs(pos0) * 11.1))
        print (pos0)
        pi.set_servo_pulsewidth(servo_0, pos0)


def servo1(pos1):
    pi.set_servo_pulsewidth(servo_1, pos1)

def servo0_off():
    pi.set_mode(servo_0, pigpio.INPUT)
        
def r_motor(rm):   

            if rm > 100:  # Make sure the value sent to the motor is 100 or less
                print("Out of range")
                rm = 100

            elif rm < -100:  # Make sure the value sent to the motor is 100 or less
                print("Out of range")
                rm = -100

            rMotor = rm * 2.55

            # Set right motor direction
            if rMotor > 0:  
                pi.write(dira, FWD)  # Go forwards
                RM = rMotor
                print("Right Motor ="),(rm)
                #print("Actual = "),(RM)

            elif rMotor < 0:  
                pi.write(dira, BWD)  # Go backwards
                RM = abs(rMotor)  # Make positive
                print("Right Motor ="),(rm)
                #print("Actual = -"),(RM)
            else:
                print("Right Stop")
                RM = 0  # Stop            
 
            pi.set_PWM_dutycycle(pwma,RM)


def l_motor(lm):  

            if lm > 100:  # Make sure the value sent to the motor is 100 or less
                print("Out of range")
                lm = 100

            elif lm < -100:  # Make sure the value sent to the motor is 100 or less
                print("Out of range")
                lm = -100

            lMotor = lm * 2.55
              
            # Set left motor direction
            if lMotor > 0:
                pi.write(dirb, FWD)  # Go forwards
                LM = lMotor
                print("Left Motor  ="),(lm)
                #print("Actual = "),(LM)
            elif lMotor < 0:  
                pi.write(dirb, BWD)  # Go backwards
                LM = abs(lMotor)  # Make positive
                print("Left Motor  ="),(lm)
                #print("Actual = -"),(LM)
            else:
                print("Left Stop")
                LM = 0  # Stop  
   
            pi.set_PWM_dutycycle(pwmb,LM)   
            
            
            
def Stop(): 
            pi.set_PWM_dutycycle(pwma,0)
            pi.set_PWM_dutycycle(pwmb,0)

            pi.set_mode(pwma, pigpio.INPUT)	
            pi.set_mode(pwmb, pigpio.INPUT)

            pi.stop() 
    

