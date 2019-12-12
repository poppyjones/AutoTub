from RPi import GPIO

relay_GPIO = 17
state = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_GPIO,GPIO.OUT, initial=state)

def on():
    state = 1
    GPIO.output(relay_GPIO,state)

def off():
    state = 0
    GPIO.output(relay_GPIO,state)
