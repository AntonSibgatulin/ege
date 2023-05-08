file= open("files/26 (1).txt")
N = int(file.readline())

numbers = list([int(i) for i in file])

count = 0
max_ = -10**11
for x in range(len(numbers)-1):
    f = numbers[x]
    if f%2!=0:
        continue
    for y in range(x+1,len(numbers)):
        s = numbers[y]
        if s%2!= 0:
            continue
        if ((f+s)//2) in numbers:
            count+=1
            max_ = max(max_,(f+s)//2)
print(count,max_)