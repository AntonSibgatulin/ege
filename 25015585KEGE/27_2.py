import math

file = open("files/27-A_3231.txt")

N = int(file.readline())
arr = [int(i) for i in file]
max_ = 10**10
index = 0
size = N//2
for x in range(len(arr)):
    summ = 0

    arr_new = arr[slice(x + (len(arr) + 1) // 2, len(arr))]
    arr_new.extend(arr[slice(0, x + (len(arr) + 1) // 2)])
    if x > len(arr) / 2:
        arr_new = arr[slice(x - (len(arr)) // 2, len(arr))]
        arr_new.extend(arr[slice(0, x - (len(arr) ) // 2)])

    #print(arr[x], arr_new)
    for i in range(len(arr_new)):
        leng = abs(i - size )
        if x>len(arr)/2:
            leng = abs(size-i)
        summ += leng * arr_new[i]
        #if x == 7:
            #print(leng, arr_new[i])
    if summ <= max_:
        index = x
        max_ = min(summ, max_)
print(max_, index+1)
