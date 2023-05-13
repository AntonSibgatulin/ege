file = open("files/27_A_7627.txt")
K = int(file.readline())
N = int(file.readline())

numbers = [int(i) for i in file]

summ = 0
for x in range(len(numbers)-K):
    for y in range(x+K,len(numbers)):
        f = numbers[x]
        s = numbers[y]
        summ = max(summ,f+s)
print(summ)