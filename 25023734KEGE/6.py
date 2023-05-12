import turtle as t



t.speed(5000)
t.rt(-90)
t.rt(315)

k=20
for i in range(7):
    t.fd(16*k)
    t.rt(45)
    t.fd(8*k)
    t.rt(135)

t.up()

for x in range(100):
    for y in range(15):
        t.goto(-x*k,y*k)
        t.dot(4)