for A in range(1000):
    count = 0
    for x in range(200):
        for y in range(200):
            if (x>=9) or (2*x<y) or (x*y<A):
                count+=1
    if count == 200*200:
        print(A)
        break