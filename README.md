# sumobot

I initially tried to base my robot off [this kit](https://www.fingertechrobotics.com/proddetail.php?prod=ft-cobra-chassis), 
but it is backordered and they may never get any more according to the owner.  
I ended up ordering [this subset](https://www.fingertechrobotics.com/proddetail.php?prod=ft-cobra-chassis-no-pcb), 
but the base is awfully heavy so I am going to drill holes in it to lighten it so I can get more batteries in. (500g limit for mini-class) 
I replaced half the PCB with [these components](https://www.amazon.com/gp/product/B085XSLKFQ/ref=ppx_yo_dt_b_asin_title_o09_s00?ie=UTF8&psc=1) but be warned that they are big.
They are also cheap and easy to work with.  They also provide 5v out so I use them to power my motors and my Pi off the 5v out and just feed them off a battery pack.

I also bought some things I haven't used yet so I can do line and enemy detection in v2 

*Diligent.com* 
- Pmod AD2: 4-channel 12-bit A/D Converter  410-2171 
- Pmod LVLSHFT: Logic Level Shifter  410-320 

*Sparkfun.com* 
- SparkFun RedBot Sensor - Line Follower SEN-117693 (2) 
- Ultrasonic Distance Sensor - HC-SR04 SEN-15569 

I plan to switch from a Pi2b to a Pi Zero WH so I can do bluetooth and wireless more easily.  The bluetooth dongle I had laying around is one of the things I haven't 
got working yet.  Most of the other people I know are using Arduino but I didn't have one and haven't used one before.


I also got several packages of wiring sets and a breadboard off Amazon: 
- https://www.amazon.com/gp/product/B07ZMGJM17/ref=ppx_yo_dt_b_asin_title_o08_s00?ie=UTF8&psc=1 
- https://www.amazon.com/gp/product/B08SL9X2YC/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1 
- https://www.amazon.com/gp/product/B06XKWDSPT/ref=ppx_yo_dt_b_asin_title_o05_s00?ie=UTF8&psc=1 
- https://www.amazon.com/gp/product/B07FXBPD2G/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1 

##Additional project links:
- https://www.ev3dev.org/docs/tutorials/using-ps3-sixaxis/ 
- https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/ 
- https://www.etechnophiles.com/l298n-motor-driver-pin-diagram/ 
- https://github.com/splitbrain/rpibplusleaf 
- https://learn.sparkfun.com/tutorials/raspberry-gpio/introduction 
- https://www.hackster.io/austin-stanton/raspberry-pi-sumobot-767fde?ref=channel&ref_id=425_trending___&offset=25 
- https://forum.pololu.com/t/new-mini-sumo-project/12072/3 
- https://www.instructables.com/Raspberry-Pi-SumoBot/ 
- https://www.raspberrypi.org/documentation/usage/gpio/ 
- https://theraspberryblonde.wordpress.com/2016/06/29/ps3-joystick-control-with-pygame/ 
- https://www.etechnophiles.com/l298n-motor-driver-pin-diagram/https://www.instructables.com/Raspberry-PI-L298N-Dual-H-Bridge-DC-Motor/ 
- https://www.piborg.org/blog/joyborghttps://github.com/gavinlyonsrepo/RpiMotorLib 
- https://www.instructables.com/How-to-Make-Arduino-Sumo-Robot/ 
- https://www.instructables.com/Simple-Arduino-and-HC-SR04-Example/ 
- https://thepihut.com/blogs/raspberry-pi-tutorials/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pihttps://tutorials-raspberrypi.com/raspberry-pi-ultrasonic-sensor-hc-sr04/ 
