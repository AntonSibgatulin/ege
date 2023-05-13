from fnmatch import *


for x in range(0,10**8,211):
    if fnmatch(str(x),"11??4*56"):
        print(x,x//211)