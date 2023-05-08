def f(x,h):
    if x>=151 and h==4:
        return 1
    elif x<151 and h ==4:
        return 0
    elif x>=151 and h<4:
        return 0
    else:
        if h%2 == 0:
            return f(x + 1, h + 1) and f(x + 2, h + 1) and f(x * 2, h + 1)
        else:
            return f(x + 1, h + 1) or f(x + 2, h + 1) or f(x * 2, h + 1)

for x in range(1,150):
    if f(x,1)==1:
        print(x)