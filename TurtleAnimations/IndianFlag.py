import turtle

# Set up the turtle
turtle.speed(30)
turtle.bgcolor("white")
turtle.title("Indian Flag")

# Function to draw a rectangle
def draw_rectangle(width, height, color):
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()


# Draw the flag components
def draw_indian_flag():
    width = 900
    height = 600
    middle_rect_height = height / 3
    ashoka_chakra_diameter = middle_rect_height
    content_1 = -height / 2 + 650  # Position to write content
    content_2 = -height / 2 - 50

    # Draw saffron rectangle
    turtle.penup()
    turtle.goto(-width / 2, height / 2)
    turtle.pendown()
    draw_rectangle(width, middle_rect_height, "#FF9933")

    # Draw white rectangle
    turtle.penup()
    turtle.goto(-width / 2, middle_rect_height / 2)
    turtle.pendown()
    draw_rectangle(width, middle_rect_height, "white")

    # Draw green rectangle
    turtle.penup()
    turtle.goto(-width / 2, -middle_rect_height/2)
    turtle.pendown()
    draw_rectangle(width, middle_rect_height, "#138808")

    # Draw Ashoka Chakra
    turtle.pensize(5)
    turtle.penup()
    turtle.goto(0, -middle_rect_height/2)
    turtle.pendown()
    turtle.color("blue")
    turtle.circle(ashoka_chakra_diameter / 2)
    for _ in range(24):
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.forward(ashoka_chakra_diameter / 2)
        turtle.backward(ashoka_chakra_diameter / 20)
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.left(360 / 24)

    # Write content under the Chakra
    turtle.penup()
    turtle.goto(0, content_1)
    turtle.pendown()
    turtle.color("black")
    turtle.write("Happy 77th Independence Day", align="center", font=("Arial",45, "bold"))
    turtle.penup()
    turtle.goto(0, content_2)
    turtle.pendown()
    turtle.color("black")
    turtle.write("From Code to Canvas: Python Animation Magic - by pytech.academy ", align="center", font=("Arial", 20, "bold"))

# Draw the Indian flag
draw_indian_flag()

# Hide the turtle
turtle.hideturtle()

# Keep the window open until it's closed by the user
turtle.done()