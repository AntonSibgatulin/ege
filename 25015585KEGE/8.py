import itertools

alp = '0123456'
num = '0246'
alphabet = itertools.product(alp, repeat=5)
count = 0
for x in alphabet:
    if x.count("5") != 1 or x[0]=='0': continue
    flag = True
    for j in range(1, len(x) - 1):
        if (x[j] == '5') and (x[j + 1] in num or x[j - 1] in num ):
            flag = False
            break
    if x[0] == '5':
        if x[1] in num:
            flag = False
    if x[-1] == '5':
        if x[-2] in num:
            flag = False

    if flag:
        count += 1

print(count)
