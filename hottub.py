from datetime import datetime
from time import sleep
import temp_sensor


interval = 10                 #interval between tests (sec)
min_temp = 25                 #celcius
standby_temp = min_temp + 5   #celcius


def raise_temp(goal):
    while True:
        curr = temp_sensor.current_temperature()
        if(curr >= goal):
            print("GOAL REACHED!")
            #do relay stuff!
            return
        sleep(interval-1) 


def standby_mode():
    while True:
        if(temp_sensor.current_temperature() < min_temp):
            print("TOO COLD TRIGGER RELAY: " + str(datetime.now().strftime("%H:%M:%S")))
            raise_temp(standby_temp)
        else:
            print("temp fine")
        print(str(temp_sensor.current_temperature()))
        sleep(interval)



#this is the start!
standby_mode()
