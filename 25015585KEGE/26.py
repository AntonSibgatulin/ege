file = open("files/26_5141.txt")

N = int(file.readline())
M = int(file.readline())

arr = [int(i) for i in file]
arr.sort()
arr2 = arr.copy()

count = 0
summ = 0
last_index = 0
max_  =0
for x in range(len(arr)):
    i = arr[x]
    if summ + i <= M:
        summ += i
        count += 1
        last_index = x
        arr2.remove(i)
        max_ = max(max_,i)
    else:
        continue

max_summ = 0
#print(arr)
print(summ, count, last_index)
print(arr2)
print(max_)
maxi = M-summ+max_
print(maxi)

while arr2[0] < maxi:
    arr2.remove(arr2[0])
print(arr2[0])