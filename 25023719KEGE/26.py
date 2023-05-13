file = open("files/26_7626.txt")

K = int(file.readline())
N = int(file.readline())

arr = [0]*K
a = []
for x in range(N):
    x1,x2 = map(int,file.readline().split(" "))
    a.append([x1,x2])

a.sort()
print(a)

def check(a):
    for i in range(len(arr)):
        x = arr[i]
        if x==0 or x<a :
            return i
    return -1
last = -1
count = 0
for x in a:
    l = check(x[0])
    if l != -1:
        arr[l] = x[1]
        count+=1
        last = l
print(count,last+1)


