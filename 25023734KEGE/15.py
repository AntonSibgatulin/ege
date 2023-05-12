for a in range(1, 10000):
    count = 0
    for x in range(0, 500):
        if (x & 39) == 0 or ((x & 11) == 0) <= ((x & a) != 0):
            count += 1
    if count == 500:
        print(a)
        break
