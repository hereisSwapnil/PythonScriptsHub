from turtle import Turtle

TIMS = []
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.tims = TIMS
        self.create_snake()
        self.head = self.tims[0]

    def grow(self):
        self.tims.append(Turtle(shape="square"))
        self.tims[-1].pu()
        self.tims[-1].color("white")
        self.tims[-1].width(20)
        self.tims[-1].goto(self.tims[-2].xcor(), self.tims[-2].ycor())

    def create_snake(self):
        for n in range(3):
            self.tims.append(Turtle(shape="square"))
            self.tims[n].pu()
            self.tims[n].color("white")
            self.tims[n].width(20)
            self.tims[n].goto(-n * 20, 0)

    def reset(self):
        for n in self.tims:
            n.goto(1000, 1000)
        TIMS.clear()
        self.tims = TIMS
        self.create_snake()
        self.head = self.tims[0]

    def move(self):
        for n in range(len(self.tims) - 1, 0, -1):
            self.tims[n].goto(self.tims[n - 1].xcor(), self.tims[n - 1].ycor())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
