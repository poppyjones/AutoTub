from datetime import datetime

print("Hello! This script was called: ")
print(str(datetime.now().strftime("%d %b %Y %H:%M:%S")) + "\n")
# the terminal willremain open whilethe script is running
input() # the script stops once it receives input 