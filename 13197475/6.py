import turtle as t

k=20

t.rt(-90)
t.speed(500)

for x in range(6):
    t.rt(36)
    t.fd(10*k)
    t.rt(36)

t.up()

for x in range(100):
    for y in range(20):
        t.goto(x*k,y*k-10*k)
        t.dot(4)

t.done()