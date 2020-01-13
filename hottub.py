from time import sleep
from utilities import writeerror
from utilities import timestring
import temp_sensor
import relay
import sys


intervalOFF  = 20*60          #interval between tests (sec)
intervalON   = 5*60           #interval between tests (sec)
standby_min  = 3              #celcius
standby_max = standby_min + 1 #celcius


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

def maintain_temp(min_temp, max_temp):
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
    maintain_temp(standby_min,standby_max)