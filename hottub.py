from time import sleep
from utilities import writeerror
from utilities import timestring
import temp_sensor
import relay
import sys


intervalOFF  = 20*60    #interval between tests (sec)
intervalON   = 5*60     #interval between tests (sec)
min_temp     = 3        #celcius
max_temp = min_temp + 1 #celcius


def raise_temp(goal):
    relay.on()
    #TODO add timeout
    try:
        while True:
            sleep(intervalON) 
            curr = temp_sensor.current_temperature()
            if(curr >= goal):
                print("GOAL REACHED!")
                relay.off()
                return
            print("TOO COLD: " + timestring())
            print(str(temp_sensor.current_temperature()))
    except Exception as err:
        print(err)
        writeerror(err+timestring())
        sys.exit()

def standby_mode():
    try:
        while True:
            print(str(temp_sensor.current_temperature()))
            if(temp_sensor.current_temperature() < min_temp):
                print("TOO COLD TRIGGER RELAY: " + timestring())
                raise_temp(max_temp)
                continue
            else:
                print("temp fine")
            sleep(intervalOFF)
    except Exception as err:
        print(err)
        writeerror(err+timestring())
        sys.exit()



if __name__ == "__main__":
    standby_mode()