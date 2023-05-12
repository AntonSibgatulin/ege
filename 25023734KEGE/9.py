file = open("files/09_7588.csv")


def check(array):
    string = " "+str(array[0]) + " " + str(array[1]) + " " + str(array[2]) + " " + str(array[3]) + " " + str(array[4])+" "
    if string.count(" "+str(array[0])+ " ") > 1:
        return False
    elif string.count(" "+str(array[1])+ " ") > 1:
        return False
    elif string.count(" "+str(array[2])+ " ") > 1:
        return False
    elif string.count(" "+str(array[3])+ " ") > 1:
        return False
    elif string.count(" "+str(array[4])+ " ") > 1:
        return False
    else:
        return True


def checkNum(array):
    summ = sum(array)
    sum_another = (summ - max(array) - min(array)) * 2
    max_min_summ = (max(array) + min(array)) * 3
    if max_min_summ <= sum_another:
        return True
    else:
        return False


numbers = []
for x in range(3200):
    f1, f2, f3, f4, f5 = (map(int, file.readline().split(",")))
    arr = [f1, f2, f3, f4, f5]
    numbers.append(arr)

count = 0
for x in numbers:
    if check(x) and checkNum(x):
        count += 1
print(count)
