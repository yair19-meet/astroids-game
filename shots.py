import turtle

SCREEN_WIDTH = int(turtle.getcanvas().winfo_width()) // 2
SCREEN_HEIGHT = int(turtle.getcanvas().winfo_height()) // 2

#turtle.register_shape("rocket", ((0, 20), (5, 25), (10, 20), (10, 0), (0, 0))

turtle.hideturtle()

arrow = turtle.clone()
arrow.shape("arrow")
arrow.setheading(90)
arrow.showturtle()
arrow.penup()

def move():
    while arrow.ycor() < SCREEN_HEIGHT - 10:
        current_y = arrow.ycor()
        new_y = arrow.ycor() + 2
        arrow.goto(arrow.xcor(), new_y)


SPACE = "space"

turtle.onkey(move, SPACE)

turtle.listen()
    



