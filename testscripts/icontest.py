from datetime import datetime

print("Great! It looks like the icons are working: ")
print(str(datetime.now().strftime("%d %b %Y %H:%M:%S")) + "\n")
# the terminal will remain open while the script is running
input() # the script stops once it receives input 