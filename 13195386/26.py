import operator

file = open("files/26.txt")

consingment , money = map(int,file.readline().split(" "))

A = []

B = []
for x in range(consingment):
    j = file.readline().split(" ")
    price = int(j[0])
    count = int(j[1])
    category = j[2]
    if category == "A":
        A.append([price,count])
    else:
        B.append([price,count])
#A.sort()
#B.sort()

A = sorted(A, key = lambda x: (x[0], x[1]))
B = sorted(B, key = lambda x: (x[0], x[1]))

print(A)
print(B)

for x in range(len(A)):
    #if money - A[x][0]*A[x][1] >= 0:
    money = money - A[x][0]*A[x][1]

countB = 0
for x in range(len(B)):
    if money - B[x][0] * B[x][1] >= 0:
        countB+=B[x][1]
        money = money - B[x][0] * B[x][1]

print(countB,money)