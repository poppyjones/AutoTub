from datetime import datetime
from time import sleep
import temp_sensor


interval = 10 #interval between tests (sec)
sensor = temp_sensor
min_temp = 25 #celcius

while True:
    if(sensor.current_temperature < min_temp):
        print("TO COLD TRIGGER RELAY: {%H:%M:%S}".format(datetime.now()))
    else:
        print("temp fine")
    sleep(interval)
    print(str(temp_sensor.current_temperature()))
