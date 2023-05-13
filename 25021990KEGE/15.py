for A in range(1,1000):
    count = 0
    for x in range(200):
        for y in range(200):
            if (x+y<=32) or (y<=x+4) or (y>=A):
                count+=1

    if count==200*200:
        print(A)
