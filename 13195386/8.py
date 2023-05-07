def to(a,b):
    string = ''
    while a>0:
        string = str(a%b)+string
        a = a//b
    return int(string)

print(to(149,4))