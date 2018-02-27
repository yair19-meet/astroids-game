import turtle
import random
import time
turtle.tracer(1,0) 
SIZE_X=900
SIZE_Y=600


turtle.setup(SIZE_X, SIZE_Y) 
#size.
turtle.penup()
SQUARE_SIZE = 50


turtle.register_shape("Space_Shipp.gif")




START_LENGTH = 1
#Initialize lists

space = turtle.clone()
space.goto(0,-200)
space.shape("Space_Shipp.gif")

turtle.hideturtle()


arrow_circle = turtle.clone()
arrow_circle.shape('circle')




LEFT_ARROW="Left"
RIGHT_ARROW="Right"
SPACEBAR="space"
TIME_STEP=0



LEFT=0
DOWN=1
RIGHT=2



SCREEN_WIDTH = int(turtle.getcanvas().winfo_width()) // 2
SCREEN_HEIGHT = int(turtle.getcanvas().winfo_height()) // 2

turtle.hideturtle()

arrow = turtle.clone()
arrow.shape("arrow")
arrow.setheading(90)
arrow.penup()

def move():
    bool = False
    arrow.goto(space.xcor(), space.ycor())
    arrow_circle.goto(arrow.xcor(), arrow.ycor())
    arrow.showturtle()
    while arrow.ycor() < SCREEN_HEIGHT - 10:
        current_y = arrow.ycor()
        new_y = arrow.ycor() + 0.25
        arrow.goto(arrow.xcor(), new_y)
        arrow_circle.goto(arrow.xcor(), arrow.ycor())

        if arrow.ycor() > SCREEN_HEIGHT - 60:
            arrow.color("orange")

        if arrow.ycor() > SCREEN_HEIGHT - 15:
            bool = True


#    Color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

 #   r = random.randrange(0, 257, 10)
 #   g = random.randrange(0, 257, 10)
 #   b = random.randrange(0, 257, 10)
    
    arrow.color("black")
    if bool:
     #   arrow.hideturtle()
     #   turtle.bgcolor("orange")
     #   turtle.forward(10000)
    #    turtle.bgcolor("white")

        arrow.hideturtle()

        turtle.color("black", "orange")
        arrow.penup()
        turtle.penup()
        turtle.begin_fill()
        turtle.goto(arrow.xcor() - 10, SCREEN_HEIGHT)
        turtle.goto(arrow.xcor() - 10, -700)
        turtle.goto(arrow.xcor() + 15, -700)
        turtle.goto(arrow.xcor() + 15, SCREEN_HEIGHT)
        turtle.goto(arrow.xcor() - 10, SCREEN_HEIGHT)
        turtle.end_fill()
        turtle.forward(20000)
        turtle.reset()

        turtle.hideturtle()
        






def left():
    global direction
    direction=LEFT
    current_x=space.xcor()
    new_x=space.xcor()-10
    space.goto(new_x,space.ycor())
    print("you pressed the left key!")



def right():
    global direction
    direction=RIGHT
    current_x1=space.xcor()
    new_x1=space.xcor()+10
    space.goto(new_x1,space.ycor())
    print("you pressed the right key!")


SPACE = "space"

turtle.onkey(move, SPACE)


turtle.onkey(left, LEFT_ARROW)
turtle.onkey(right, RIGHT_ARROW)
turtle.listen()


turtle.mainloop()

