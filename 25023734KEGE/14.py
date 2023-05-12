for x in '0123456789ABCD':
    summ = int('97968'+x+'13',15) + int('7'+x+'213',15)
    if summ%14 == 0:
        print(summ//14)
        break