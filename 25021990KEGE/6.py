import turtle as t

k =20

t.speed(500)

t.rt(-90)


for x in range(4):
    t.fd(10*k)
    t.rt(270)

t.up()


t.fd(3*k)
t.rt(270)
t.fd(5*k)
t.rt(90)


t.down()



for x in range(2):
    t.fd(10*k)
    t.rt(270)
    t.fd(12*k)
    t.rt(270)

t.up()

for x in range(100):
    for y in range(25):
        t.goto(-x*k,y*k)
        t.dot(4)