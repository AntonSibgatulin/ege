file = open("files/26_3377 (1).txt")

N = int(file.readline())

numbers = [[] for x in range(10000)]

for x in range(N):
    x, y = map(int, file.readline().split(" "))
    # numbers.append([x,y])
    numbers[x].append(y)
    numbers[x].sort()
max_ = -10 ** 10
count = 0
index = 0
for o in range(len(numbers)):
    x = numbers[o]
    summ = 0
    if len(x) <= 1:
        continue
    for l in range(len(x) - 1):
        f = x[l]
        s = x[l + 1]
        if s - f > 2:
            summ += (s - f) // 2
    if summ>=max_:
        max_ = summ
        index = o
    if summ>0:
        count+=summ

print(count,index)
