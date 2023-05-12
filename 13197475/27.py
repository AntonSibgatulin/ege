file = open("files/107_27_A.txt")
N = int(file.readline())

numbers = [int(i) for i in file]

min_ = 10**10
index = 0
for x in range(len(numbers)):
    summ = 0
    for k in range(len(numbers)):
        summ+=abs(x-k)*numbers[k]
    if(min_>summ):
        index=x
        min_ = min(min_,summ)
print(index,min_)