import re
fil='./regex_sum_2241109.txt'
hand=open(fil)
num=list()
for line in hand:
    li=line.rstrip()
    b=re.findall('[0-9]+',li)
    if len(b)<1:
            continue
    for c in b:
          a=int(c)
          num.append(a)
print(sum(num))
   