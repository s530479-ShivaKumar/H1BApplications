s = open("./Output/sortoutput.txt","r")   
r = open("./Output/r.txt", "w")   

thisKey = ""
thisValue = 0.0
count = 0
for line in s:
 data = line.strip().split('\t')
 store, amount = data

 if store != thisKey:
   if thisKey:
     # output the last key value pair result
    r.write(thisKey + '\t' + str(thisValue)+'\n')
    count = count + 1
    if count < 5:
      print(thisKey + '\t' + str(thisValue)+'\n')      
   # start over when changing keys
   thisKey = store
   thisValue = 0.0
 # apply the aggregation function
 thisValue += int(amount)
r.write(thisKey + '\t' + str(thisValue)+'\n')

s.close()
r.close()

