from datetime import datetime
from time import sleep
import temp_sensor
import relay

interval = 10                 #interval between tests (sec)
min_temp = 25                 #celcius
standby_temp = min_temp + 5   #celcius


def raise_temp(goal):
    relay.on()
    #TODO add timeout
    while True:
        sleep(interval) 
        curr = temp_sensor.current_temperature()
        if(curr >= goal):
            print("GOAL REACHED!")
            relay.off()
            return
        print("TOO COLD: " + str(datetime.now().strftime("%H:%M:%S")))
        print(str(temp_sensor.current_temperature()))




def standby_mode():
    while True:
        print(str(temp_sensor.current_temperature()))
        if(temp_sensor.current_temperature() < min_temp):
            print("TOO COLD TRIGGER RELAY: " + str(datetime.now().strftime("%H:%M:%S")))
            raise_temp(standby_temp)
        else:
            print("temp fine")
        sleep(interval)



#this is the start!
standby_mode()
