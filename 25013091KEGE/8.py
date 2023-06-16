from itertools import *

a = 'KATER'
arr = product(a,repeat=3)

count = 0
for x in arr:
    if x.count("R") == 2:
        count+=1
print(count)