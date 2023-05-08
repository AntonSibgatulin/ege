maths = (49**6) *(7**19)-7**9-21


def to(a,b):
    string = ''
    while a>0:
        string = str(a%b)+string
        a=a//b
    return (string)


print(to(maths,7).count("6"))