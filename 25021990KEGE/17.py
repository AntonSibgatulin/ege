file = open("files/17_6752.txt")

numbers = [int(i) for i in file]

count_del_3 = 0

for x in numbers:
    if (x%3 == 0):
        count_del_3 +=1
count = 0
max_ = -10**10

for x in range(len(numbers)-1):
    f = numbers[x]
    s = numbers[x+1]
    if (f<0 or s<0) and (f+s)<count_del_3:
        count +=1
        max_ = max(max_,f+s)

print(count,max_)