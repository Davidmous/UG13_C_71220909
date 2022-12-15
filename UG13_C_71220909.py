import turtle
s = turtle.Screen()
s.bgcolor('blue')
t = turtle.Turtle()
t.pencolor('cyan')
t.pensize(10)

#D
t.penup()
t.goto(-250, -150)
t.pendown()
t.circle(90,180)
t.left(90)
t.forward(180)
t.penup()

#0
t.goto(-90, 100)
t.pendown()
t.left(180)
t.circle(-75,180)
t.forward(50)
t.circle(-75,180)
t.forward(50)





s.exitonclick()
