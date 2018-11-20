mapinput = open("./Output/mapout.txt", "r")
sortoutput = open("./Output/sortoutput.txt", "w")
lines = mapinput.readlines()
lines.sort()

for line in lines:
	sortoutput.write(line)
mapinput.close()
sortoutput.close()

