# This line of code will open a input file to read only
input = open("./Output/sorted.txt","r")
# This line of code will open output file to write only
output = open("./Output/reducer.txt","w")
# These multiple lines of code will iterate through each line of input and calculate the total number of the common value
thisKey = ""
thisValue = 0
index=0
for line in input:
    #This line of code will split the csv record to a tuple by comma 
    record = line.strip().split(",")
    if len(record) == 2:
        states, value = record
        if states.strip() != thisKey:
            if thisKey:
                #These lines of code will give the last key value pair as an Output
                output.write(thisKey.strip() + ' ' + str(thisValue)+'\n')
                index=index+1
                #This line of code will run if the index is below 15
                if index <  40:
                    print(thisKey.strip() + ' ' + str(thisValue)+'\n')
            #This line of coe will help the app to start over when changing keys
            thisKey = states.strip()
            thisValue = 0
        thisValue += float(value)
#These lines of code will output the final entry
output.write(thisKey.strip() + ' ' + str(thisValue)+'\n')
input.close()
output.close()