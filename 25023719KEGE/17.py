file = open("files/17_7619.txt")



numbers = [int(i) for i in file]


def length(a):
    return len(str(a))
max_2 = -10**10
for x in numbers:
    if length(x) == 2:
        max_2 = max(max_2,x)


count = 0
max_ = -10**10
for x in range(len(numbers)-1):
    f = numbers[x]
    s = numbers[x+1]
    if ( (length(f) == 2 and length(s)!=2) or (length(s) == 2 and length(f)!=2) ) and (f+s)%max_2 == 0:
        count+=1
        max_ = max(max_,f+s)

print(count,max_)
