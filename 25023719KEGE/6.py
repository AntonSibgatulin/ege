import turtle as t

k=20



t.speed(6000)
t.rt(-90)
t.rt(45)

for x in range(7):
    t.fd(6*k)
    t.rt(45)
    t.fd(12*k)
    t.rt(135)

t.up()


for x in range(1000):
    for y in range(15):
        t.goto(x*k,y*k)
        t.dot(4)