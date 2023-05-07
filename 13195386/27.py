file = open("files/27-B_demo.txt")

count = int(file.readline())
numbers = []
summ = 0
minimum = 10**10
for l in range(count):
    line = file.readline()
    x, y = map(int, line.split(" "))
    #if (summ+min(x))%3!=0:
    summ +=min(x,y)
    if abs(x-y)%3 != 0:
        minimum = min(minimum,y-x)

if summ%3!=0:
    print(summ)
else:
    print(summ-minimum)