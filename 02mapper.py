# venkatesh vemula
# practice mapper

f = open("purchases.txt","r")  # open file, read-only
o = open("out02.txt", "w") # open file, write
for line in f:  
    rowList = line.strip().split("    ") 
    print (rowList )
    print (len(rowList ))
    if len(rowList) == 6:
        date, time, location, dept, amount, payType = rowList  #assign names
        print ("{0}\t{1}".format(amount, location))
        o.write("{0}\t{1}\n".format(amount, location))
f.close()
o.close()