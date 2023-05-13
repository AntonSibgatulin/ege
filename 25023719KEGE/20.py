def f(x, h):
    if x >= 43 and h == 4:
        return 1
    if x < 43 and h == 4:
        return 0
    if x >= 43 and h < 4:
        return 0
    else:
        if h % 2 != 0:
            return f(x + 1, h + 1) or f(x + 4, h + 1) or f(x * 3, h + 1)
        else:
            return f(x + 1, h + 1) and f(x + 4, h + 1) and f(x * 3, h + 1)

for x in range(1,43):
    if f(x,1) == 1:
        print(x)



