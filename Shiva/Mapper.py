f = open("../Data/H1B.csv","r")  # open file, read-only
o = open("./Output/MapperOutput.txt", "w") # open file, write
count = 0
#for each line in the data
for line in f:  
    data = line.strip().split(",") 
    if len(data) == 15 and len(data[1])>0: 
        o.write("{0},{1}\n".format(data[1].strip(), 1))
        count = count + 1
        # just for printing 5 values
        if count < 5:
                print("{0},{1}\n".format(data[1], 1))
f.close() #close the file
o.close() #close the file