for x in '0123456789ABCD':
    m = int('97968'+x+'15',15)+int('7'+x+'233',15)
    if m%14 == 0:
        print(m//14)
        break