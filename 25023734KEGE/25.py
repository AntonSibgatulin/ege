from fnmatch import *

for x in range(0,10**8+1,273):
    if fnmatch(str(x),'12??36*1'):
        print(x,x//273)