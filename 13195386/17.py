file = open("files/17.txt")

numbers = [int(i) for i in file]
min_del = 1000000000000
for x in numbers:
    if len(str(x))==3 and str(x)[2]=='5':
        min_del = min(min_del,x)
print(min_del)
def lenw(a):
    return len(str(a))
min_ = 10000000
count = 0
for x in range(len(numbers)-1):
    f = numbers[x]
    s = numbers[x+1]
    if ((lenw(f) == 3 and lenw(s)!=3) or (lenw(s) == 3 and lenw(f)!=3 )) and (f+s)%min_del ==0:
        count+=1
        min_ = min(min_,f+s)
print(count,min_)