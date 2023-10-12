import turtle

pen = turtle.Turtle()
screen = turtle.Screen()

pen.hideturtle()
pen.penup()
pen.goto(-154, 4)
pen.pendown()
pen.showturtle

#orange box
pen.color("#f25022")
pen.begin_fill()
pen.goto(-204, 4)
pen.goto(-204, 50)
pen.goto(-154, 50)
pen.goto(-154, 4)
pen.end_fill()

#green box
pen.color("#7fba00")
pen.penup()
pen.goto(-150, 4)
pen.pendown()
pen.begin_fill()
pen.goto(-150, 50)
pen.goto(-100, 50)
pen.goto(-100, 4)
pen.goto(-150, 4)
pen.end_fill()

#yellow box
pen.color("#ffb900")
pen.penup()
pen.goto(-150, 0)
pen.pendown()
pen.begin_fill()
pen.goto(-100, 0)
pen.goto(-100, -50)
pen.goto(-150, -50)
pen.goto(-150, 0)
pen.end_fill()

#blue box
pen.color("#00a4ef")
pen.penup()
pen.goto(-154, 0)
pen.pendown()
pen.begin_fill()
pen.goto(-204, 0)
pen.goto(-204, -50)
pen.goto(-154, -50)
pen.goto(-154, 0)
pen.end_fill()

pen.hideturtle()
