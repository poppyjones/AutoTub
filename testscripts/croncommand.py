from datetime import datetime
from pathlib import Path

def foo():  
    f_path = str(Path(__file__).parent.absolute()) + "/logs/crontest.log"
    print(f_path)
    f = open(f_path, "a")
    f.write("The command ran at: ")
    f.write(str(datetime.now()))
    f.write("\n")
    f.close()