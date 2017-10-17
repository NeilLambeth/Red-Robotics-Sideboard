# Red Robotics Sideboard V1.0 (Beta)

Python library for the Red Robotics 'Sideboard' Raspberry Pi add on robotics board.

Simple python commands for motor control and Neopixels. 



##Installation:

In the Raspberry Pi terminal type:

`curl -L https://raw.githubusercontent.com/NeilLambeth/Red-Robotics-Sideboard/master/setup.sh | bash`

This can take around 10 minutes on a Pi2 on a fresh install of Raspian Lite.  



##Basic usage:

Open up a python shell with:  
`Sudo python`

Load the neopixel module:

`from neopixels import *`

Then try these:

`red()`

`blue()`

`green()`  

To mix colours -  
`setColour(0,255,0,255)`  (LED number, red value, green value, blue value)


Attach more Neopixels to the 3pin header, pin closest to the led is +v then Data then Ground. 

With eight led's attached - try:  
`knightRider()`

To clear:  
`clear()`  


##Motors

`from sideboard import *`

Right motor full speed forwards:

`r_motor(100)` 

Right motor half speed forwards:

`r_motor(50)`

Right motor full speed backwards:

`r_motor(-50)`

Right motor stop:

`r_motor(0)`


Left motor full speed forwards:

`l_motor(100)`

Left motor stop:

`l_motor(0)`


##Reset/Shutdown switch

Short press- less than a second: LED will just flash yellow

Medium press - between 1 and 4 seconds: LED turns orange - Pi resets

Long press - greater than 4 seconds: LED turns red - Pi shutsdown


Wait 20 seconds before sliding the power switch to make sure the Pi has had enough time to shutdown.
