def to(a,b):
    string = ''
    while a>0:
        string = str(a%b)+string
        a=a//b
    return string

for x in range(2,1000):
    N = to(x,2)
    summ = sum(list(map(int, list(N))))
    if(summ%2 == 0):
        N =( N+'1').replace(N[0]+N[1],'10',1)
    else:
        N = (N + '11').replace(N[0] + N[1], '1', 1)
    R = int(N,2)
    if R>=100:
        print(x,R)
        break