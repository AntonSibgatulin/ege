import math

file = open("files/27_A_5142.txt")

N,M = map(int , file.readline().split(" "))


roads = [0]*1000
print(roads)

for i in file:
    x,y = map(int,i.split(" "))
    roads[x-1]=y
print(roads)

max_ = 0
index = 0

for x in range(len(roads)):
    count = 0
    if roads[x] == 0:continue
    for i in range(x-M,x+M+1):
        if i<0 or i>=len(roads):
            continue
        count+=roads[i]
    if count>=max_:
        max_ = count
        index = x

print(index,max_)
c = 0
for x in range(index-M,index+M+1):
    c+=math.ceil(roads[x]/50)
print(c)