import turtle

wn=turtle.Screen()
turtle.bgcolor('white')
turtle.color('red')
turtle.shape('turtle')
t5=turtle.Turtle()
move=1

###############################
t5.speed("fastest")
for i in range(10):
    for i in range(4):
          t5.pu()
          t5.goto(500,200)
          t5.pd()
          t5.color('orange')
          t5.pensize(3)
          t5.circle(50,steps=4)
          t5.right(100)
          
t5.speed("fastest")
for i in range(6):
    for i in range(4):
          t5.pu()
          t5.goto(0,0)
          t5.pd()
          t5.color('red')
          t5.pensize(3)
          t5.circle(100,steps=6)
          t5.right(100)

turtle.done()