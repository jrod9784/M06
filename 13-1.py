from datetime import *
now = datetime.now()
print(now)
f = open("today.txt", "w")
f.write(str(now))
f.close()
