for x in '0123456789ABC':
    summ = int('4C'+x+'4',15)+int(x+'62A',13)
    if summ%121==0:
        print(summ//121)
        break