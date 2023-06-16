
for x in range(100,1000):
    string = str(x)
    i1 = int(string[0]+string[1])
    i2 = int(string[1] + string[2])
    i3 = int(string[0] + string[2])
    if i1 * i1 == x:
        print(x, i1, i1)
    if i2*i2 == x:
        print(x,i2,i2)
    if i3 * i3 == x:
        print(x, i3, i3)
    if i1 * i2 == x:
        print(x, i1, i2)
    if i1*i3 == x:
        print(x,i1,i3)
    if i2*i3 == x:
        print(x,i3,i2)
