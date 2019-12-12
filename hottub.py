from datetime import datetime
from time import sleep
import temp_sensor
import relay

intervalOFF  = 20*60    #interval between tests (sec)
intervalON   = 5*60     #interval between tests (sec)
min_temp     = 5        #celcius
max_temp = min_temp + 2 #celcius


def raise_temp(goal):
    relay.on()
    #TODO add timeout
    while True:
        sleep(intervalON) 
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
            raise_temp(max_temp)
        else:
            print("temp fine")
        sleep(intervalOFF)



#this is the start!
standby_mode()
