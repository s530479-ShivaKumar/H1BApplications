# open Input file in Read Mode
input = open("./Output/sortoutput.txt","r", encoding="utf-8")
# open output file in write mode
output = open("./Output/reducerout.txt","w", encoding="utf-8")
# Iterate through each line of input and calculate sum for each category for all records
thisKey = ""
thisValue = 0.0
row = 1
for index,line in enumerate(input, start=1):
    # split the csv record to a tuple
    record = line.strip().split(",")
    # check whether the length of a record is 2 to avoid dirty data
    if len(record) == 2:
        soc_code, value = record
        if soc_code.strip() != thisKey:
            if thisKey:
                # output the last key value pair result
                output.write(thisKey.strip() + ',' + str(thisValue)+'\n')
                if index < 50:
                    print(thisKey.strip() + '\t' + str(thisValue)+'\n')
            # start over when changing keys
            thisKey = soc_code.strip()
            thisValue = 0.0
        # apply the aggregation function
        thisValue += float(value)
# output the final entry
output.write(thisKey.strip() + ',' + str(thisValue)+'\n')
input.close()
output.close()