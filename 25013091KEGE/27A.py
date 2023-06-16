file = open("files/27A_2724.txt")

N = int(file.readline())
numbers = [int(x) for x in file]


count = 0
for i in range(len(numbers)-1):
    for j in range(i+1,len(numbers)):
        f = numbers[i]
        s = numbers[j]
        if (f+s) % 131 == 0:
            count+=1
print(count)