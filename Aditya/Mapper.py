f = open("../Data/H1B.csv","r")  # open file, read-only
o = open("./Output/mapout.txt","w") # open file, write

count =0

for line in f:  
    data = line.strip().split(",") 
    #print data
    #print len(data)
    if len(data) == 15 and len(data[0]) > 0:
    
    # print "{0}\t{1}".format(data(0), 1)
        o.write("{0}\t{1}\n".format(data[0], 1))
        count = count +1
        if count < 5 :
                print("{0}\t{1}\n".format(data[0], 1))

f.close()
o.close()