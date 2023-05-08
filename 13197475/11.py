def to(a,b):
    string = ''
    while a>0:
        string = str(a%b)+string
        a=a//b
    return (string)
print(len(to(2999,2)))