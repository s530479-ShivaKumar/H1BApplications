mapinput = open("./Output/mapout.txt", "r", encoding="utf-8")
sortoutput = open("./Output/sortoutput.txt", "w", encoding="utf-8")
lines = mapinput.readlines()
lines.sort()

for line in lines:
	sortoutput.write(line)
mapinput.close()
sortoutput.close()

