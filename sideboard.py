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
    if pos0 >= 0 and pos0 <91:
        print ("servo0 ="),(pos0)
        pos0 = 1500 - (pos0 * 11.1)
        #print (pos0)
        pi.set_servo_pulsewidth(servo_0, pos0)
    
    elif pos0 < 0 and pos0 >-91:
        print ("servo0 ="),(pos0)
        pos0 = (abs(pos0) * 11.1) + 1500
        #print (pos0)
        pi.set_servo_pulsewidth(servo_0, pos0)

    else:
        print ("Out Of Range!")

def servo0_P(pos0):
    if pos0 >499 and pos0 <2501:
        print ("servo0 ="),(pos0)
        pi.set_servo_pulsewidth(servo_0, pos0)

    else:
        print ("Out Of Range!")

def servo0_off():
    pi.set_servo_pulsewidth(servo_0, 0)
    print ("servo0 off")



 
def servo1(pos1):
    if pos1 >= 0 and pos1 <91:
        print ("servo1 ="),(pos1)
        pos1 = 1500 - (pos1 * 11.1)
        #print (pos1)
        pi.set_servo_pulsewidth(servo_1, pos1)
    
    elif pos1 < 0 and pos1 >-91:
        print ("servo1 ="),(pos1)
        pos1 = (abs(pos1) * 11.1) + 1500
        #print (pos1)
        pi.set_servo_pulsewidth(servo_1, pos1)

    else:
        print ("Out Of Range!")


def servo1_P(pos1):
    if pos1 >499 and pos1 <2501:
        print ("servo1 ="),(pos1)
        pi.set_servo_pulsewidth(servo_1, pos1)

    else:
        print ("Out Of Range!")

def servo1_off():
    pi.set_servo_pulsewidth(servo_1, 0)
    print ("servo1 off")





       
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
                print("Right Motor ="),(rm),("\r")
                #print("Actual = "),(RM)

            elif rMotor < 0:  
                pi.write(dira, BWD)  # Go backwards
                RM = abs(rMotor)  # Make positive
                print("Right Motor ="),(rm),("\r")
                #print("Actual = -"),(RM)
            else:
                print("Right Stopstop\r")
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
                print("Left Motor  ="),(lm),("\r")
                #print("Actual = "),(LM)
            elif lMotor < 0:  
                pi.write(dirb, BWD)  # Go backwards
                LM = abs(lMotor)  # Make positive
                print("Left Motor  ="),(lm),("\r")
                #print("Actual = -"),(LM)
            else:
                print("Left Stop\r")
                LM = 0  # Stop  
   
            pi.set_PWM_dutycycle(pwmb,LM)   
            
  
          
            
def Stop(): 
            pi.set_PWM_dutycycle(pwma,0)
            pi.set_PWM_dutycycle(pwmb,0)

            pi.set_mode(pwma, pigpio.INPUT)	
            pi.set_mode(pwmb, pigpio.INPUT)

            pi.stop() 
    

