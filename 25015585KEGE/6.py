import turtle as t
k=20
t.rt(-90)
t.speed(400)
for x in range(10):
    t.fd(10*k)
    for y in range(2):
        t.fd(10*k)
        t.rt(90)

t.up()

for x in range(1000):
    for y in range(50):
        t.goto(x*k,y*k)
        t.dot(4)

t.done()