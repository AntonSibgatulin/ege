for A in range(1,1000):
    count = 0

    for m in range(100):
        for n in range(100):
            if (2*m+3*n>40) or ((m<A) and(n<=A)):
                count+=1
    if count==100*100:
        print(A)
        break