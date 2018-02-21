import turtle

SCREEN_WIDTH = int(turtle.getcanvas().winfo_width()) // 2
SCREEN_HEIGHT = int(turtle.getcanvas().winfo_height()) // 2

turtle.hideturtle()

arrow = turtle.clone()
arrow.shape("arrow")
arrow.setheading(90)
arrow.penup()

def move():
    arrow.goto(0, 0)
    arrow.showturtle()
    while arrow.ycor() < SCREEN_HEIGHT - 10:
        current_y = arrow.ycor()
        new_y = arrow.ycor() + 2
        arrow.goto(arrow.xcor(), new_y)
    arrow.hideturtle()


SPACE = "space"

turtle.onkey(move, SPACE)

turtle.listen()

turtle.mainloop()
    



