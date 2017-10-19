import time
import pigpio

# Setup GPIO
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

print("Sideboard loaded")


        
def r_motor(rMotor):   

            # Set right motor direction
            if rMotor > 0:  
                pi.write(dira, FWD)  # Go forwards
                RM = rMotor
                print ("Right Motor = "),(RM)
            elif rMotor < 0:  
                pi.write(dira, BWD)  # Go backwards
                RM = abs(rMotor)  # Make positive
                print("Right Motor = -"),(RM)
            else:
                print("Right Stop")
                RM = 0  # Stop
            
            pi.set_PWM_dutycycle(pwma,RM)


def l_motor(lMotor):                
            # Set left motor direction
            if lMotor > 0:
                pi.write(dirb, FWD)  # Go forwards
                LM = lMotor
                print("Left Motor  = "),(LM)
            elif lMotor < 0:  
                pi.write(dirb, BWD)  # Go backwards
                LM = abs(lMotor)  # Make positive
                print("Left Motor  = -"),(LM)
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
    

