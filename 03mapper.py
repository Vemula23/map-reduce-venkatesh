# Mapper

import sys 


for line in sys.stdin:
  datalist = line.strip().split(",")

  if (len(datalist) == 3) : 
    TEAM,W,L = datalist

    print(TEAM,"\t",W)

