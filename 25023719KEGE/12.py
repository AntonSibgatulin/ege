for n in range(4,1000):
    string = '3'+'5'*n
    while '25' in string or '355' in string or '555' in string:
        if '25' in string:
            string = string.replace("25","32",1)
        if '355' in string:
            string = string.replace("355","25",1)
        if '555' in string:
            string = string.replace('555','3',1)
    numbers = [int(i) for i in string]

    if sum(numbers) == 17:
        print(n)
        break
