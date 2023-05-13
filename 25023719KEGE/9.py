file = open('files/9.csv')

numbers=[]

def check(arr):
    error = [i for i in arr if arr.count(i)>1]
    return len(error) == 0

def checkNum(arr):
    summ = (sum(arr)-max(arr)-min(arr))
    max_and_min = 2*(max(arr)+min(arr))
    return max_and_min>=summ


for x in range(17000):
    x1,x2,x3,x4,x5 = map(int,file.readline().split(";"))
    numbers.append([x1,x2,x3,x4,x5])

count = 0

for x in numbers:
    if check(x) and checkNum(x):
        count+=1

print(count)