def to(a,b):
    string = ''
    while a>0:
        string = str(a%b)+string
        a = a//b
    return int(string)
a = []
for x in range(100,3001):
    maths = str(to(x,2))
    maths = maths.replace("1","",1)
    while maths.startswith("0"):
        maths = maths.replace("0","",1)
    if len(maths)==0:
        maths= '0'
    res = x - int(maths,2)
    if not(res in a):
        a.append(res)
print(len(a))