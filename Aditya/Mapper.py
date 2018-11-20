f = open("../Data/H1B.csv","r")  # open the file in read-only mode
o = open("./Output/mapout.txt","w") # open the file in  write mode

# initial count is 0
count =0

# Iterate each line in f
for line in f:  
#Split the record 
    data = line.strip().split(",") 
#Check the length of the data
    if len(data) == 15 and len(data[0]) > 0:
        o.write("{0}\t{1}\n".format(data[0], 1))
        #Check whether the count is less than 5 and print the data in console
        count = count +1
        if count < 5 :
                print("{0}\t{1}\n".format(data[0], 1))

f.close() # Close the f file
o.close() # CLose the o file