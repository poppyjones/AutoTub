from datetime import datetime

f = open("tempLog.txt", "a")
f.write("Hello! This script was called: ")
f.write(str(datetime.now().strftime("%d %b %Y %H:%M:%S")) + "\n")
f.write("   The temprature was: {0:0.3f}C\n".format(sensor.temprature))
f.close()