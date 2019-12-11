from datetime import datetime

f = open("helloLog.txt", "a")
f.write("Hello! This script was called: ")
f.write(str(datetime.now().strftime("%d %b %Y %H:%M:%S")) + "\n")
f.close()