import time
import os
import pigpio
import neopixels
 
 
button = 8
buttonPress = False
startTime = 0
elaspedTime = 0

#os.system('sudo pigpiod')
 
neopixels.red()
time.sleep(.5)

neopixels.green()
time.sleep(.5)

neopixels.blue()
time.sleep(.5)

neopixels.clear()

#connect to pigpiod daemon
pi = pigpio.pi()
 
# setup pin as an input
pi.set_mode(button, pigpio.INPUT)
pi.set_pull_up_down(button, pigpio.PUD_UP)

print ("Shutdown Script Running!") 

while True:
    try:
      time.sleep(0.1)  
      # Time the button press
      if pi.read(button) == False and buttonPress == False:
          neopixels.setColour(0,127,127,0)
          buttonPress = True
          startTime = time.time()
          print("Button Press") 
          time.sleep(0.1)
       
      #print length of button press
      if pi.read(button) == False:
          #print("Button Held") 
          runningTime = time.time()
          elaspedTime = runningTime-startTime
          #print(round(elaspedTime,1))

      #Check for button release
      if pi.read(button) == True and buttonPress == True:
          neopixels.setColour(0,0,0,0)
          print("Button Release")
          buttonPress = False
          print(round(elaspedTime,1))
          
          if elaspedTime >1 and elaspedTime <4:
              print("Reboot")  
              neopixels.setColour(0,0,0,0) 
              os.system('shutdown -r now')  # Reboot
              time.sleep(1)
              print("Exit") 
              exit()
              
          elif elaspedTime >3:
              print("Shutdown")
              neopixels.red()
              time.sleep(0.5)   
              neopixels.setColour(0,0,0,0)
              os.system('shutdown -h now')  # Shutdown
              time.sleep(1) 
              print("Exit") 
              exit()
              
      if elaspedTime >1 and elaspedTime <4:
              neopixels.setColour(0,255,127,0)
              #print("Short Press")   
              
              
      elif elaspedTime >3:
          neopixels.red()  
          #print("Long Press")
          
                      
    except KeyboardInterrupt: 
        #disconnect
        pi.stop()
        exit()
