# Red Robotics Sideboard V1.0 (Beta)

Python library for the Red Robotics 'Sideboard' Raspberry Pi add on robotics board.

Simple python commands for motor control and Neopixels. 




## Installation:

In the Raspberry Pi terminal, copy and paste:

`curl -L https://raw.githubusercontent.com/NeilLambeth/Red-Robotics-Sideboard/master/setup.sh | bash`

This can take around 10 minutes on a Pi2 on a fresh install of Raspian Lite.  
On a PiZero it takes about 35 minutes.



## Basic usage:

Open up a python shell with:  
`sudo python`

Load the neopixel module:  
`from neopixels import *`  
Wait for the neopixels module to load


To set the on-board neopixel to full red type:

`red()`

This also works with blue and green:

`blue()`

`green()`  

If you want different colours, use:  
`setColour(0,128,0,128)`  
This will give you purple. The first value is the position of the neopixel (0 for the one on the Sideboard).  
The next three numbers are the red, green and blue values.

For white:  
`setColour(0,255,255,255)`

Orange:  
`setColour(0,255,165,000)`

Yellow:  
`setColour(0,255,255,0)`  
    
### Other neopixel commands

You can fade red up and down with:  
`heartbeat()`
__Ctrl + c__ to stop

Attach more Neopixels to the 3pin header, pin closest to the led is +v then Data then Ground. 

With eight led's attached - try:  
`knightRider()`
__Ctrl + c__ to stop


To turn all neopixels off:  
`clear()`  

  

## Motors

`from sideboard import *`

Right motor full speed forwards:  
`r_motor(100)` 

Right motor half speed forwards:  
`r_motor(50)`

Right motor full speed backwards:  
`r_motor(-100)`

Right motor stop:  
`r_motor(0)`

Left motor full speed forwards:  
`l_motor(100)`

Left motor stop:  
`l_motor(0)`

## Servos (Headboard only)  

`from sideboard import *`

You can connect two servos - servo0 and servo1

Set the angle of the servo directly - to set the servo to the centre position:  
`servo0(0)`

Or for servo1:  
`servo1(0)`

90 degrees:  
`servo0(90)`

-45 degrees  
`servo0(-45)`

If you prefer, you can set the servo position by the pulse width.
Minimum value is 500, max is 2500.

Centre:  
`servo0_P(1500)`

+90 degrees:  
`servo0_P(500)`

-45 degrees:  
`servo0_P(2000)`

-90 degrees:  
`servo0_P(2500)`

Cut the power to the servo with:  
`servo0_off()`

## Reset/Shutdown switch

Short press- less than a second: LED will just flash yellow

Medium press - between 1 and 4 seconds: LED turns orange - Pi resets

Long press - greater than 4 seconds: LED turns red - Pi shutsdown


Wait 20 seconds before sliding the power switch to make sure the Pi has had enough time to shutdown.
