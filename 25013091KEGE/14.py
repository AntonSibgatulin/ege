for x in '0123456789ABCD':
    math = int("9897"+x+"21",15)+int("12"+x+"023",15)
    if math%14 ==0:
        print(math//14)