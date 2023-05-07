import turtle as t

t.rt(-90)


k = 20


for x in range(6):
    t.fd(10*k)
    t.rt(60)

t.up()

for x in range(100):
    for y in range(25):
        t.goto(x*k,y*k-6*k)
        t.dot(4)