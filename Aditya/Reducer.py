s = open("./Output/sortoutput.txt","r")   # open the file in read-only mode
r = open("./Output/r.txt", "w")   # open the file in  write mode

thisKey = ""
thisValue = 0.0

#Initial count is 0
count = 0
# Iterate each line in s
for line in s:
  #Split the csv record
 data = line.strip().split('\t')
 datefiled, amount = data

 if datefiled != thisKey:
   if thisKey:
     # output the last key value pair result
    r.write(thisKey + ',' + str(thisValue)+'\n')
    count = count + 1
      #Check whether the count is less than 5 and print the data in console
    if count < 5:
      print(thisKey + '\t' + str(thisValue)+'\n')      
   # start over when changing keys
   thisKey = datefiled
   thisValue = 0.0
 # apply the aggregation function
 thisValue += int(amount)

 #Output
r.write(thisKey + ',' + str(thisValue)+'\n')

s.close() #close the s file
r.close() #close the r file

