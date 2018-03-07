import turtle
import random 
turtle.tracer(1,0) 
SIZE_X=900
SIZE_Y=600


turtle.setup(SIZE_X, SIZE_Y) 
#size.
turtle.penup()
SQUARE_SIZE = 50





START_LENGTH = 1
#Initialize lists

space = turtle.clone()
space.goto(0,-200)
space.color("blue")
space.shape("circle")

turtle.hideturtle()







LEFT_ARROW="Left"
RIGHT_ARROW="Right"
SPACEBAR="space"
TIME_STEP=0



LEFT=0
DOWN=1
RIGHT=2




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




turtle.onkey(left, LEFT_ARROW)
turtle.onkey(right, RIGHT_ARROW)
turtle.listen()







       
