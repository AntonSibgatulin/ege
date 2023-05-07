for x in range(489421,489440):
    arr = []
    flag = True
    for j in range(1,round(x**0.5)+1):
        if x%j == 0:
            arr.append(x//j)
            arr.append(j)
        if len(arr)>4:
            flag = False
            break
    if flag and len(arr)==4:
        print(sorted(arr))

