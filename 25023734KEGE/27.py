file = open("files/27A_7603.txt")
N = int(file.readline())
K = int(file.readline())


numbers = [int(i) for i in file]
max_ = -10**10
for x in range(len(numbers)-K):
    for y in range(x+K,len(numbers)):
        f = numbers[x]
        s = numbers[y]
        max_ = max(f+s,max_)
print(max_)