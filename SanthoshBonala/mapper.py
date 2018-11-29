import re
# open Input file in Read Mode
input = open("../Data/H1B.csv","r", encoding="utf-8")
# open output file in write mode
output = open("./Output/mapout.txt","w", encoding="utf-8")
# Iterate through each line of input and print soc_code,1 for all records
for index,line in enumerate(input, start=1):
    # split the csv record to a tuple
    record = line.strip().split(",")
    # check whether the length of a record is 15 to avoid dirty data
    if len(record) == 15 and re.compile("[0-9]{2}-[0-9]+").match(record[7]):
            # output the soc_code along with 1 to perform addition in reducer phase
            output.write("{0},{1}\n".format(record[7], 1))
            if index < 5:
                    print("{0},{1}\n".format(record[7], 1))
input.close()
output.close()