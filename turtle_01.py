import turtle

t = turtle.Turtle()
t.shape("turtle")
s = t.clone()
s.hideturtle()

t.speed(1)
t.lt(45)
t.penup();t.goto(-300, -300);t.pendown()

t.penup();t.goto(300, 300);t.pendown()

s.penup();s.goto(50, -50);s.pendown();s.goto(-50, 50)

turtle.done()
