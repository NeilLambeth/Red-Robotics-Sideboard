# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time

from neopixel import *
print("neopixels loaded")



# LED strip configuration:
LED_COUNT      = 9     # Number of LED pixels.
LED_PIN        = 12      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 127     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

red = 0
green = 0
blue = 0


# Define functions which animate LEDs in various ways.
def clear():
	for i in range(strip.numPixels()):
		strip.setPixelColor(i,0)
		strip.show()

def Blue():
        strip.setPixelColorRGB(0, 0,0,255) 
        strip.show()

def Green():
        strip.setPixelColorRGB(0, 0,255,0) 
        strip.show()

def Red():
        strip.setPixelColorRGB(0, 255,0,0) 
        strip.show()        

def setColour(P,R,G,B):
        strip.setPixelColorRGB(P,R,G,B) 
        strip.show()

def fadeSingle():
        red = 0
        while True:
                #Fade up one red LED
                for i in range(0, 255):# Count from 0 to 255 - 255 is the max brightness for the NeoPixels
                    red = red + 1 #Increase red brightness    
                    strip.setPixelColorRGB(0, red,0,0) 
                    strip.show()
                    time.sleep(0.01)
                    
                        
                #Fade Down one red LED        
                for i in range(0, 255):# Count to 255    
                    red = red - 1 #Decrease red brightness
                    strip.setPixelColorRGB(0, red,0,0) 
                    strip.show()
                    time.sleep(0.01)        

def knightRider():
    while True:
        for i in range(1,strip.numPixels()-1):
                strip.setPixelColorRGB(i, 255,0,0) 
                strip.show()
                time.sleep(0.1)
                clear()
			
        for i in range(strip.numPixels()-1,1,-1):  
                strip.setPixelColorRGB(i, 255,0,0)
                strip.show()
                time.sleep(0.1)
                clear()



# Main program logic follows:
#if __name__ == '__main__':
# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
# Intialize the library (must be called once before other functions).
strip.begin()

	

