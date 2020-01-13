from datetime import datetime
from w1thermsensor import W1ThermSensor
sensor = sensor = W1ThermSensor()

#f = open("tempLog.txt", "a")
#f.write("Hello! This script was called: ")
#f.write(str(datetime.now().strftime("%d %b %Y %H:%M:%S")) + "\n")
#f.write("   The temperature was: {0:0.3f}C\n".format(sensor.temperature))
#f.close()

print("   The temperature is: {0:0.3f}C\n".format(sensor.get_temperature()))


input()