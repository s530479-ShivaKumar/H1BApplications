mapinput = open("./Output/mapout.txt", "r") # Open the file in read only mode
sortoutput = open("./Output/sortoutput.txt", "w") #Open the file in write mode

#reading each line
lines = mapinput.readlines()
# Sort thr lines
lines.sort()
#for each line in lines
for line in lines:
	sortoutput.write(line)

mapinput.close() #close the mapinput file
sortoutput.close() #close the sortoutput file

