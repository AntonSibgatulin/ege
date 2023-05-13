def to(a,b):
    string = ""
    while a>0:
        string = str(a%b) + string
        a=a//b
    return string
max_ = 0
for x in range(1,9):
    string = to(x,2)
    if x%2 == 0:
        string = '10'+string
    else:
        string = '1'+string+'01'
    res = int(string,2)
    max_=max(max_,res)
print(max_)