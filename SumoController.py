import RPi.GPIO as GPIO
import evdev

leftrearin1 = 13
leftrearin2 = 19
leftrearspeed = 26

leftfrontin1 = 17
leftfrontin2 = 27
leftfrontspeed = 22

rightrearin3 = 16
rightrearin4 = 20
rightrearspeed = 21

rightfrontin3 = 14
rightfrontin4 = 15
rightfrontspeed = 18

leftrearpwm = 0
rightrearpwm = 0
leftrearpwm = 0
rightrearpwm = 0

leftforward = True
rightforward = True



## Some helpers ##
def scale(val, src, dst):
    """
    Scale the given value from the scale of src to the scale of dst.

    val: float or int
    src: tuple
    dst: tuple

    example: print(scale(99, (0.0, 99.0), (-1.0, +1.0)))
    """
    return (float(val - src[0]) / (src[1] - src[0])) * (dst[1] - dst[0]) + dst[0]

def scale_stick_to_motor(value):
    return scale(value,(0,255),(-100,100))

def gpio_setup():
    ## Setup ##
    GPIO.setmode(GPIO.BCM)
    GPIO.gpio_prep(leftrearin1)
    GPIO.gpio_prep(leftrearin2)
    GPIO.gpio_prep(rightrearin3)
    GPIO.gpio_prep(rightrearin4)
    GPIO.gpio_prep(leftfrontin1)
    GPIO.gpio_prep(leftfrontin2)
    GPIO.gpio_prep(rightfrontin3)
    GPIO.gpio_prep(rightfrontin4)



def gpio_prep(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

def pwm_prep(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    p = GPIO.PWM(pin, 1000)
    p.start(0)
    return p

def stop(pin1,pin2):
    GPIO.output(pin1, GPIO.LOW)
    GPIO.output(pin2, GPIO.LOW)
    
def forward(pin1,pin2):
    GPIO.output(pin1, GPIO.HIGH)
    GPIO.output(pin2, GPIO.LOW)

def backward(pin1,pin2):
    forward(pin2, pin1)
    

## Initializing ##
print("Finding ps3 controller...")
devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
for device in devices:
    if device.name == 'PLAYSTATION(R)3 Controller':
        ps3dev = device.fn

gpio_setup()
gamepad = evdev.InputDevice(ps3dev)

leftrearpwm = pwm_prep(leftrearspeed)
rightrearpwm = pwm_prep(rightrearspeed)
leftfrontpwm = pwm_prep(leftfrontspeed)
rightfrontpwm = pwm_prep(rightfrontspeed)



for event in gamepad.read_loop():   #this loops infinitely
    value = event.value
    if event.type == 3:             #A stick is moved
        if event.code == 5:         #Y axis on right stick
            if 0.01 > value > -0.01:
                rightspeed = 0
                stop(rightfrontin3,rightfrontin4)
                stop(rightrearin3,rightrearin4)
            elif value > 0:
                # go forward
                forward(rightfrontin3,rightfrontin4)
                forward(rightrearin3,rightrearin4)
                rightspeed = value * 100
            else:
                #go backward
                backward(rightfrontin3,rightfrontin4)
                backward(rightrearin3,rightrearin4)
                rightspeed = value * 100
                
            leftrearpwm.ChangeDutyCycle(rightspeed)
            leftfrontpwm.ChangeDutyCycle(rightspeed)
        elif event.code == 1:         #Y axis on left stick
            if 0.01 > value > -0.01:
                leftspeed = 0
                stop(leftfrontin1,leftfrontin2)
                stop(leftrearin1,leftrearin2)
        elif value > 0:
            # go forward
            forward(leftfrontin1,leftfrontin2)
            forward(leftrearin1,leftrearin2)
            leftspeed = value * 100
        else:
            #go backward
            backward(leftfrontin1,leftfrontin2)
            backward(leftrearin1,leftrearin2)
            leftspeed = value * 100

        leftrearpwm.ChangeDutyCycle(leftspeed)
        leftfrontpwm.ChangeDutyCycle(leftspeed)
    if event.type == 1 and event.code == 291 and event.value == 1:
        print("Start button is pressed. Stopping.")
        running = False
        break

