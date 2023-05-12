def to(a,b):
    string = ''
    while a>0:
        string = str(a%b)+string
        a=a//b
    return string

for N in range(4,1000000):
    x = to(N,2)
    if (N%3 == 0):
        x= x+x[-3]+x[-2]+x[-1]
    else:
        x = x+to((N%3)*3,2)
    #print(int(x,2))
    if int(x,2) <100:
        print(N)