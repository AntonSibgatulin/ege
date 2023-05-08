file = open("files/09.csv")

count = 0
for x in range(5000):
    line = file.readline()
    a,b,c = map(int,line.split(","))
    d1 = max(a,b,c)**2
    e1 = min(a,b,c)**2+(sum([a,b,c]) - min(a,b,c)-max(a,b,c))**2
    if(d1<e1):
        count+=1
    #if(a+b>c and a+c>b and b+c>a):
    #    count+=1
print(count)