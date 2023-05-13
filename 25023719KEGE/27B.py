file = open("files/27_B_7627.txt")
K = int(file.readline())
N = int(file.readline())

numbers = [int(i) for i in file]

n = max(numbers)
max_ = 0
index = numbers.index(n)
for x in range(index,N):
    if abs(index-x)>=K:
        max_ = max(max_,n+numbers[x])
print(max_)