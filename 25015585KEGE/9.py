file = open("files/9_5126 (1).csv")

arr = [list(map(int,i.split(","))) for i in file]

def getRepeatData(arr):
    for x in arr:
        if arr.count(x) == 3:
            return x

count = 0
for x in range(len(arr)):
    main = arr[x]
    flag = True
    summ = 0

    for j in main:
        co = main.count(j)
        if co == 3 or co ==1:
            summ+=co
        else:
            flag = False
            break

    if flag==False:
        continue

    if summ == 12:
        #then ok
        summ2 = (sum(main)-getRepeatData(main)*3)/3
        summ3 = getRepeatData(main)*3
        if(summ2<=summ3):
            count+=1
        pass
print( count)