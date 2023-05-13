file = open("files/09_6744.csv")

count = 0
for x in range(3200):
    x1,x2,x3,x4 = map(int,file.readline().split(","))
    arr = [x1,x2,x3,x4]
    summ_another = sum(arr)-max(arr)-min(arr)
    summ_max_min = max(arr)+min(arr)
    if summ_max_min<summ_another:
        count+=1
print(count)