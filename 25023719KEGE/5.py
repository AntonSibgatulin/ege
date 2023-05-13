def to(a,b):
    string = ''
    while a>0:
        string = str(a%b)+string
        a=a//b
    return string


for x in range(4,1000):
    string = to(x,2)
    if x%3 == 0:
        string = string+string[-3]+string[-2]+string[-1]
    else:
        string = string+to((x%3)*3,2)

    if int(string,2)>76:
        print(x)
        break