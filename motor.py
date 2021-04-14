import RPi.GPIO as GPIO

leftrearin3 = 13
leftrearin4 = 19
leftrearspeed = 26
temp1 = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(leftrearin3, GPIO.OUT)
GPIO.setup(leftrearin4, GPIO.OUT)
GPIO.setup(leftrearspeed, GPIO.OUT)
GPIO.output(leftrearin3, GPIO.LOW)
GPIO.output(leftrearin4, GPIO.LOW)
p = GPIO.PWM(leftrearspeed, 1000)
p.start(25)
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")

while (1):

    x = input()

    if x == 'r':
        print("run")
        if (temp1 == 1):
            GPIO.output(leftrearin3, GPIO.HIGH)
            GPIO.output(leftrearin4, GPIO.LOW)
            print("forward")
            x = 'z'
        else:
            GPIO.output(leftrearin3, GPIO.LOW)
            GPIO.output(leftrearin4, GPIO.HIGH)
            print("backward")
            x = 'z'


    elif x == 's':
        print("stop")
        GPIO.output(leftrearin3, GPIO.LOW)
        GPIO.output(leftrearin4, GPIO.LOW)
        x = 'z'

    elif x == 'f':
        print("forward")
        GPIO.output(leftrearin3, GPIO.HIGH)
        GPIO.output(leftrearin4, GPIO.LOW)
        temp1 = 1
        x = 'z'

    elif x == 'b':
        print("backward")
        GPIO.output(leftrearin3, GPIO.LOW)
        GPIO.output(leftrearin4, GPIO.HIGH)
        temp1 = 0
        x = 'z'

    elif x == 'l':
        print("low")
        p.ChangeDutyCycle(25)
        x = 'z'

    elif x == 'm':
        print("medium")
        p.ChangeDutyCycle(50)
        x = 'z'

    elif x == 'h':
        print("high")
        p.ChangeDutyCycle(75)
        x = 'z'


    elif x == 'e':
        GPIO.cleanup()
        break

    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
