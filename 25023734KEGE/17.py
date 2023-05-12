file = open('files/17_7596.txt')

numbers = [int(i) for i in file]

min_num = 10 ** 10

for x in numbers:
    if len(str(x)) == 3 and str(x)[-1] == '5':
        min_num = min(x, min_num)


def length(n):
    return len(str(n))


min_ = 10 ** 10
count = 0
for x in range(len(numbers) - 1):
    f = numbers[x]
    s = numbers[x + 1]
    if ((length(f) == 3 and length(s) != 3) or (length(s) == 3 and length(f) != 3)) and (f + s) % min_num==0:
        count += 1
        min_ = min(f + s, min_)
print(count, min_)
