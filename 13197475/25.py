max_ = -10**11
arr = []
max_ = 0
for x in range(84052,84131):
    j = []
    for i in range(1,round(x**0.5)):
        if (x%i ==0):
            j.append(x//i)
            j.append(i)
    if(len(j)>len(arr)):
        max_=x
        arr=j
print(len(arr),max_)