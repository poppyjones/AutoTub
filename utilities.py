import temp_sensor
from time import sleep
from pathlib import Path

def temprange(min):
    t = [None]*min
    for i in range(min):
        t[i] = temp_sensor.current_temperature()
        f.write(str(t[i])+"\n")
        sleep(5)
    print(t)
    
f_path = str(Path(__file__).parent.absolute()) + "/logs/temp.log"
f = open(f_path, "a")

print("Enter the number of minutes you wish to run the test: ")
temprange(int(input()))
print("your test is complete!")