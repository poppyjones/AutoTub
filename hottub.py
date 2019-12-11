from datetime import datetime
from time import sleep
import temp_sensor


interval = 10 #interval between tests (sec)
sensor = temp_sensor
min_temp = 25 #celcius

while True:
    if(sensor.current_temperature() < min_temp):
        print("TO COLD TRIGGER RELAY: " + str(datetime.now().strftime("%H:%M:%S")))

    else:
        print("temp fine")
    print(str(temp_sensor.current_temperature()))
    sleep(interval)
