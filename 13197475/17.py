file = open("files/17 (1).txt")


numbers = [int(i) for i in file]

max_ = -10000000000
count = 0

for x in range(len(numbers)-1):
    for y in range(x+1,len(numbers)):
        f = numbers[x]
        s = numbers[y]

        if abs(f-s)%36 == 0 and (f%13==0 or s%13==0):
            count +=1
            max_= max(max_,f-s,s-f)
print(count,max_)
