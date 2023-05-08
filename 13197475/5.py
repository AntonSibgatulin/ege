def to(a,b):
    string = ''
    while a>0:
        string = str(a%b)+string
        a=a//b
    return (string)

for x in range(105,100000):
    string = str(to(x,2))
    count_0 = string.count("0")
    count_1 = string.count("1")
    if count_0 == count_1:
        string = string + string[-1]
    else:
        if count_0 < count_1:
            string = string + "0"
        if count_1 < count_0:
            string = string + "1"
    #step 2
    count_0 = string.count("0")
    count_1 = string.count("1")
    if count_0 == count_1:
        string = string + string[-1]
    else:
        if count_0 < count_1:
            string = string + "0"
        if count_1 < count_0:
            string = string + "1"
    #step 3
    count_0 = string.count("0")
    count_1 = string.count("1")
    if count_0 == count_1:
        string = string + string[-1]
    else:
        if count_0 < count_1:
            string = string + "0"
        if count_1 < count_0:
            string = string + "1"
    res = int(string,2)
    if (res%4 == 0):
        print(x)
        break
