file = open("files/27_A_6032.txt")
N = int(file.readline())

arr = []

for i in file:
    x, y = (map(int, i.split(" ")))
    arr.append([x, y])
summ = 0
min_arr = []
minim = 10 ** 10
for i in arr:
    max_ = max(i)
    summ += max_
    min_arr.append(max_)
    if max(i) - min(i)!=0:
        minim = min(minim, max(i) - min(i))
min_arr.sort()
if summ % 13 == 0:
    summ -= minim
print(summ, min_arr)
