from datetime import datetime
from pathlib import Path
from croncommand import foo

foo()
f_path = str(Path(__file__).parent.absolute()) + "/logs/crontest.log"
print(f_path)

f = open(f_path, "a")
f.write("The script ran at: ")
f.write(str(datetime.now()))
f.write("\n")
f.write(__name__)
f.close()