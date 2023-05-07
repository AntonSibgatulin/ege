for A in range(0,100):
    count = 0
    for x in range(0,300):
        if (x & 77 ==0 or (x &12 != 0) or x&A!=0):
            count +=1
    if count == 300:
        print(A)
        break