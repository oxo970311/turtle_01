import turtle

t = turtle.Turtle()
t.shape("turtle")
s = t.clone()
s.hideturtle()

t.speed(1)
t.lt(45)
t.penup();t.goto(-300, -300);t.pendown()

t.penup();t.goto(300, 300);t.pendown()

s.pensize(5);s.penup();s.goto(50, -50);s.pendown();s.goto(-50, 50)

t.rt(180)

while True:
    t.penup()
    t.forward(5)
    x, y = t.pos()

    if -50 <= x <= 50 and -50 <= y <= 50:
        t.rt(90)
        t.forward(100)
        t.lt(90)
        t.forward(100)
        t.lt(90)
        t.forward(100)
        t.right(90)
        t.forward(350)
        break

    t.pendown()



turtle.done()

