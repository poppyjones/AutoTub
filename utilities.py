import temp_sensor
from time import sleep
from pathlib import Path
import relay

def temprange(min):
    t = [None]*min
    for i in range(min):
        f = open(f_path, "a")
        t[i] = temp_sensor.current_temperature()
        print(str(t[i])+"\n")
        f.write(str(t[i])+"\n")
        f.close()
        sleep(60)
    print(t)
    
f_path = str(Path(__file__).parent.absolute()) + "/logs/temp.log"
relay.on()
print("Enter the number of minutes you wish to run the test: ")
temprange(int(input()))
print("your test is complete!")