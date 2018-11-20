# open Input file in Read Mode
input = open("./Output/sortedoutput.txt","r")
# open output file in write mode
output = open("./Output/reducerout.txt","w")

thisKey = ""
thisValue = 0.0
count =0
# Iterating through the input
for line in input:
    # split the csv record to a tuple
    record = line.strip().split(",")
    # checking for dirty data with length
    if len(record) == 2:
        soc_code, value = record
        if soc_code.strip() != thisKey:
            if thisKey:
                # writing into the output file
                output.write(thisKey.strip() + '\t' + str(thisValue)+'\n')
                count = count + 1
                # printing the top 5 values
                if count < 5:
                    print(thisKey.strip() + '\t' + str(thisValue)+'\n')
            # when the key is changed, starts again
            thisKey = soc_code.strip()
            thisValue = 0.0
        # Aggregating the results 
        thisValue += float(value)
# Write the result into the output file
output.write(thisKey.strip() + '\t' + str(thisValue)+'\n')
input.close()
output.close()