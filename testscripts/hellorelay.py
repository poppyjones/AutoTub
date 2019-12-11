from RPi import GPIO
from time import sleep


relay_GPIO = 6
state = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_GPIO,GPIO.OUT, initial=state)

try:      
    while True:
        state = 0 if state == 1 else 1
        #print("on" if state == 1 else "false")
        GPIO.output(relay_GPIO,state)
        sleep(5)

except KeyboardInterrupt:
    print ("  Quit")
    GPIO.output(relay_GPIO,0)
    GPIO.cleanup()