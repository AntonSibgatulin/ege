file = open("files/26_7602.txt")



K = int(file.readline())
N = int(file.readline())
numbers=[]
arr = [0]*K
for x in range(N):
    x1,x2 = map(int,file.readline().split(" "))
    numbers.append([x1,x2])

numbers.sort()

def check(j):
    for i in range(len(arr)):
        x = arr[i]
        if (x == 0):
            return i
        if x < j:
            return i
    return -1


last = 0
count = 0


for x in numbers:
    if check(x[0]) != -1:
        last =check(x[0])
        arr[last] = x[1]
        count+=1


print(count,last+1)