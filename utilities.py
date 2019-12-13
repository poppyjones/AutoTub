from datetime import datetime
from pathlib import Path
from time import sleep
import temp_sensor
import relay

def temprange(min):
    t = [None]*min
    f_path = str(Path(__file__).parent.absolute()) + "/logs/temp.log"
    for i in range(min):
        f = open(f_path, "a")
        t[i] = temp_sensor.current_temperature()
        print(str(t[i])+"\n")
        f.write(str(t[i])+"\n")
        f.close()
        sleep(60)
    print(t)

def runtest():
    relay.on()
    print("Enter the number of minutes you wish to run the test: ")
    temprange(int(input()))
    relay.off()
    print("your test is complete!")

def writeerror(msg):
    f_path = str(Path(__file__).parent.absolute()) + "/logs/error.log"
    f = open(f_path, "a")
    f.write(timestring() + " " + msg)
    f.close()

def timestring():
    return str(datetime.now().strftime("%H:%M:%S"))