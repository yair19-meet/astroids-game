from turtle import *
import turtle
import random
import time

turtle.tracer(1, 0)

class Rectangle(Turtle):
    def __init__(self, width, hieght):
        Turtle.__init__(self)
        self.hideturtle()
        self.width = width
        self.hieght = hieght
        self.setheading(90)
        turtle.register_shape("rec", ((0, 0), (width, 0), (width, hieght), (0, hieght), (0, 0)))
        self.shape("rec")


arrow = Rectangle(10, 10)

red_laser = Rectangle(7, 20)

red_laser.color('red')

red_laser.penup()




moving_t = turtle.clone()
moving_t.penup()
moving_t.hideturtle()



screen = turtle.Screen()
bg = "space_bg2.gif"
screen.addshape(bg)
turtle.shape(bg)

turtle.bgcolor("yellow")

starting = turtle.clone()

starting.hideturtle()

SIZE_X = 900
SIZE_Y = 600

turtle.setup(SIZE_X, SIZE_Y)
# size.
turtle.penup()
SQUARE_SIZE = 50

START_LENGTH = 1
# Initialize lists

turtle.register_shape("Space_Shipp.gif")

space = turtle.clone()
space.hideturtle()
space.goto(0, -200)
space.shape("Space_Shipp.gif")

# turtle.hideturtle()

arrow_circle = turtle.clone()
arrow_circle.shape('circle')
arrow_circle.hideturtle()

LEFT_ARROW = "Left"
RIGHT_ARROW = "Right"
SPACEBAR = "space"
TIME_STEP = 0

LEFT = 0
DOWN = 1
RIGHT = 2

SCREEN_WIDTH = int(turtle.getcanvas().winfo_width()) // 2
SCREEN_HEIGHT = int(turtle.getcanvas().winfo_height()) // 2

press = turtle.clone()
press.hideturtle()
press.color("yellow")
press.goto(-300, 0)
turtle.showturtle()

check = False

size_of_pen = 50
# for i in range(2):
#     for i in range(30):
#         press.write("ASTROIDS GAME", font= ("Arial", size_of_pen, "bold"))
#         time.sleep(0.01)
#         press.clear()
#         size_of_pen -= 1
#
#     for i in range(30):
#         press.write("ASTROIDS GAME", font= ("Arial", size_of_pen, "bold"))
#         time.sleep(0.01)
#         press.clear()
#         size_of_pen += 1

time.sleep(0.5)
press.write("ASTROIDS GAME", font= ("Arial", size_of_pen, "bold"))
press.goto(-175, -125)
time.sleep(1)
press.write("PRESS TO START", font= ("Arial", size_of_pen//2, "bold"))

# time.sleep(1)
# press.clear()

def click(x, y):
    global check
    press.clear()
    print("ff")
    if not check:
        print("fsddwf")
        press.hideturtle()
        check = not check
        starting.pencolor("yellow")
        starting.penup()
        starting.goto(-30, 0)
        starting.write("3", font= ("Arial", 50, "bold"))
        time.sleep(1)
        starting.clear()
        starting.write("2", font= ("Arial", 50, "bold"))
        time.sleep(1)
        starting.clear()
        starting.write("1", font= ("Arial", 50, "bold"))
        time.sleep(1)
        starting.clear()



        starting.goto(-100, 0)
        for i in range(3):
            starting.write("PLAY", font= ("Arial", 50, "bold"))
            time.sleep(0.2)
            starting.clear()
            time.sleep(0.2)

        space.showturtle()
        # size_of_pen = 50
        # for i in range(2):
        #     for i in range(30):
        #         starting.write("PLAY", font= ("Arial", size_of_pen, "bold"))
        #         time.sleep(0.005)
        #         starting.clear()
        #         size_of_pen -= 1
        #
        #
        #     for i in range(30):
        #         starting.write("PLAY", font= ("Arial", size_of_pen, "bold"))
        #         time.sleep(0.005)
        #         starting.clear()
        #         size_of_pen += 1



        # turtle.hideturtle()

        # arrow = turtle.clone()
        # arrow.shape("square")
        arrow.setheading(90)
        arrow.hideturtle()
        arrow.penup()
        arrow.color("lightblue")


def move():
    bool = False
    red_laser.hideturtle()
    arrow.goto(space.xcor() - 5, space.ycor() + 15)
    arrow_circle.goto(arrow.xcor(), arrow.ycor())
    arrow.showturtle()
    turtle.penup()
    size = 10
    # print("size: " + str(size))
    while arrow.ycor() + size < SCREEN_HEIGHT:
        current_y = arrow.ycor()
        new_y = arrow.ycor() + 0.25
        # arrow.goto(arrow.xcor(), new_y)
        arrow_circle.goto(arrow.xcor(), arrow.ycor() + size)
        moving_t.forward(15)
        arrow.hieght = size
        # print(arrow.hieght)
        # print("size: " + str(size))
        turtle.register_shape("rec", ((0, 0), (arrow.width, 0), (arrow.width, arrow.hieght), (0, arrow.hieght), (0, 0)))
        arrow.shape("rec")
        size += 1
        # if arrow.ycor() + size == SCREEN_HEIGHT:
        #     moving_t.forward(100000)
        #     arrow.hideturtle()
        #     for i in range(3):
        #         moving_t.forward(10000)
        #         arrow.showturtle()
        #         moving_t.forward(10000)
        #         arrow.hideturtle()

        # if arrow.ycor() > SCREEN_HEIGHT - 60:
        #     arrow.color("orange")

        # if arrow.ycor() > SCREEN_HEIGHT - 15:
        #     bool = True

    moving_t.forward(80000)
    arrow.hideturtle()
    for i in range(3):
        moving_t.forward(10000)
        arrow.showturtle()
        moving_t.forward(10000)
        arrow.hideturtle()

    # turtle.hideturtle()
    # moving_t.forward(10000)
    # turtle.showturtle()

    #    Color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    #   r = random.randrange(0, 257, 10)
    #   g = random.randrange(0, 257, 10)
    #   b = random.randrange(0, 257, 10)

    # arrow.color("black")
    # if bool:
    #     #   arrow.hideturtle()
    #     #   turtle.bgcolor("orange")
    #     #   turtle.forward(10000)
    #     #    turtle.bgcolor("white")
    #
    #     arrow.hideturtle()
    #
    #     turtle.color("black", "orange")
    #     arrow.penup()
    #     turtle.penup()
    #     turtle.begin_fill()
    #     turtle.goto(arrow.xcor() - 10, SCREEN_HEIGHT)
    #     turtle.goto(arrow.xcor() - 10, -700)
    #     turtle.goto(arrow.xcor() + 15, -700)
    #     turtle.goto(arrow.xcor() + 15, SCREEN_HEIGHT)
    #     turtle.goto(arrow.xcor() - 10, SCREEN_HEIGHT)
    #     turtle.end_fill()
    #     turtle.forward(20000)
    #     turtle.reset()
    #
    #     turtle.hideturtle()

def shoot_red_laser():
    arrow.hideturtle()
    turtle.register_shape("rec", ((0, 0), (5, 0), (5, 20), (0, 20), (0, 0)))
    red_laser.shape("rec")
    red_laser.goto(space.xcor() - 3.5, space.ycor() + 15)
    red_laser.showturtle()
    # new_red = red_laser.clone()
    # new_red.goto(space.xcor(), space.ycor() + 15)
    # new_red.showturtle()
    while red_laser.ycor() < SCREEN_HEIGHT:
        # NEW_Y = red_laser.ycor() + 0.25
        red_laser.forward(0.1)
    red_laser.hideturtle()

def left():
    global direction
    direction = LEFT
    current_x = space.xcor()
    new_x = space.xcor() - 10
    space.goto(new_x, space.ycor())
    # print("you pressed the left key!")
    if space.xcor() <= -SCREEN_WIDTH:
        X = space.xcor()
        Y = space.ycor()
        space.hideturtle()
        space.goto(-X, Y)
        space.showturtle()


def right():
    global direction
    direction = RIGHT
    current_x1 = space.xcor()
    new_x1 = space.xcor() + 10
    space.goto(new_x1, space.ycor())
    # print("you pressed the right key!")
    if space.xcor() >= SCREEN_WIDTH:
        X = space.xcor()
        Y = space.ycor()
        space.hideturtle()
        space.goto(-X, Y)
        space.showturtle()


SPACE = "space"

turtle.onkey(move, SPACE)

turtle.onkey(left, LEFT_ARROW)
turtle.onkey(right, RIGHT_ARROW)

turtle.onkey(shoot_red_laser, 's')

turtle.listen()

turtle.onclick(click)

turtle.mainloop()

