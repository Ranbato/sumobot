import RPi.GPIO as GPIO
import evdev
import espeak

from time import sleep

leftrearin1 = 19
leftrearin2 = 13
leftrearspeed = 26

leftfrontin1 = 27
leftfrontin2 = 17
leftfrontspeed = 22

rightrearin3 = 16
rightrearin4 = 20
rightrearspeed = 21

rightfrontin3 = 14
rightfrontin4 = 15
rightfrontspeed = 18

leftfrontpwm = 0
rightfrontpwm = 0
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

    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    gpio_prep(leftrearin1)
    gpio_prep(leftrearin2)
    gpio_prep(rightrearin3)
    gpio_prep(rightrearin4)
    gpio_prep(leftfrontin1)
    gpio_prep(leftfrontin2)
    gpio_prep(rightfrontin3)
    gpio_prep(rightfrontin4)


def gpio_prep(pin):
    print(f"gpio setup {pin}")
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)


def pwm_prep(pin):
    print(f"pwm setup {pin}")
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
    
while True:
    ## Initializing ##
    espeak.init()
    speaker = espeak.Espeak()
    print("Finding ps3 controller...")
    devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
    ps3dev = None
    for device in devices:
        print(device.path, device.name, device.phys)
        if device.name == 'Sony PLAYSTATION(R)3 Controller':
            ps3dev = device.fn
            print(ps3dev)
        else:
            print("Other device")
    if ps3dev is None:
        sleep(2)
        continue

    gpio_setup()
    gamepad = evdev.InputDevice(ps3dev)

    leftrearpwm = pwm_prep(leftrearspeed)
    rightrearpwm = pwm_prep(rightrearspeed)
    leftfrontpwm = pwm_prep(leftfrontspeed)
    rightfrontpwm = pwm_prep(rightfrontspeed)



    for event in gamepad.read_loop():   #this loops infinitely
        if event.type == 3:             #A stick is moved
            value = scale_stick_to_motor(event.value)
            if event.code == 4:         #Y axis on right stick
                rightspeed = 0
    #            print(f"{value}")
                if 10 > value > -10:
                    stop(rightfrontin3,rightfrontin4)
                    stop(rightrearin3,rightrearin4)
                elif value > 1:
                    # go forward
                    forward(rightfrontin3,rightfrontin4)
                    forward(rightrearin3,rightrearin4)
                    rightspeed = abs(value)
                else:
                    #go backward
                    backward(rightfrontin3,rightfrontin4)
                    backward(rightrearin3,rightrearin4)
                    rightspeed = abs(value)
    #            print(f"right speed {rightspeed}")
                rightrearpwm.ChangeDutyCycle(rightspeed)
                rightfrontpwm.ChangeDutyCycle(rightspeed)
            elif event.code == 1:         #Y axis on left stick
                leftspeed = 0
     #           print(f"{value}")
                if 10 > value > -10:
                    stop(leftfrontin1,leftfrontin2)
                    stop(leftrearin1,leftrearin2)
                elif value > 1:
                    # go forward
                    forward(leftfrontin1,leftfrontin2)
                    forward(leftrearin1,leftrearin2)
                    leftspeed = abs(value)
                else:
                    #go backward
                    backward(leftfrontin1,leftfrontin2)
                    backward(leftrearin1,leftrearin2)
                    leftspeed = abs(value)
    #            print(f"left speed {leftspeed}")
                leftrearpwm.ChangeDutyCycle(leftspeed)
                leftfrontpwm.ChangeDutyCycle(leftspeed)
        elif event.type == 1 and event.value == 1:
            say = "Uh Oh"
            if event.code == 307: say = "Exterminate!"
            elif event.code == 308: say = "You will be defeated!"
            elif event.code == 304: say = "Run away!"

            speaker.say(say)
            print(f"Bbutton is pressed: {event.code}.")
        #     running = False
        #     break
    sleep(1)
