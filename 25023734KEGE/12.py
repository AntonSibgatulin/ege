for n in range(4,1000):
    string = '3'+'5'*n
    while '25' in string or '355' in string or '555' in string:
        if '25' in string:
            string = string.replace("25","3",1)
        if '355' in string:
            string = string.replace('355','52',1)
        if '555' in string:
            string = string.replace("555","23",1)



    numbers = []
    for x in string:
        numbers.append(int(x))
    summ = sum(numbers)
    if (summ ==27):
        print(n)
        break
