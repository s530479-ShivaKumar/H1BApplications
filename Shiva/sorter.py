mapperinput = open("./Output/MapperOutput.txt", "r") # open file read only
sortedoutput = open("./Output/sortedoutput.txt", "w") # write into file
lines = mapperinput.readlines() # reading the each line
lines.sort() #sort the data
#for each line of data in the input data
for line in lines:
	sortedoutput.write(line)
mapperinput.close() # close the mapper file
sortedoutput.close() # close the sortedoutput file

