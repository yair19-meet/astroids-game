from turtle import *
import turtle
import random
import time
import math


turtle.tracer(1, 0)


class Asteroids(Turtle):
    def __init__(self,x,y,dy,r,color):
        Turtle.__init__(self)
        self.penup()
        self.goto(x, y)
        self.dy = dy
        self.x = x
        self.r = r
        self.left(90)
        self.color(color)
        self.shape("circle")

    def moveball(self):
        current_y = self.ycor()
        new_y = current_y + self.dy
        down_side_asteroids = new_y - self.r            
        if(down_side_asteroids == -SCREEN_HEIGHT):
          self.goto(self.x,SCREEN_HEIGHT)

        self.goto(new_x,new_y)

          
    def MoveDown(self):
        # it moves the balls down while there is no collision between the balls and the arrow and the ground
       # a = self.y-1
       # self.y = a
       # self.goto(self.x,a)
       self.forward(-1)
       turtle.update()

def collide(arrow_circle, astroid):
    D = math.sqrt(math.pow(arrow_circle.xcor()-astroid.xcor(), 2) + math.pow(arrow_circle.ycor()-astroid.ycor(),2))
    sum_r= int((arrow_circle.shapesize()[0])/10)+astroid.r
    if(D+10<=sum_r):
       return True
    return False
    #if D < astroid.r:
        #return True
        #print("TRUETRUE")
    #return False


MAXIMUM_BALL_RADIUS = 20
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_Dy = 5
MINIMUM_BALL_Dy = 3
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
ASTEROIDS=[]

def check_astroid_collision(self):
    for astroid in ASTEROIDS:
        if collide(arrow_circle,astroid):
            print("collide")
            X=random.randint(round(-SCREEN_WIDTH)+MAXIMUM_BALL_RADIUS, round(SCREEN_WIDTH) - MAXIMUM_BALL_RADIUS)
            Y= random.randint(SCREEN_HEIGHT,SCREEN_HEIGHT+80)
            astroid.goto(X,Y)


class Rectangle(Turtle):
    def __init__(self, width, hieght):
        Turtle.__init__(self)
        self.hideturtle()
        self.width = width
        self.hieght = hieght
        self.setheading(90)
        turtle.register_shape("rec", ((0, 0), (width, 0), (width, hieght), (0, hieght), (0, 0)))
        self.shape("rec")




def CREATEBALLS():
    NUMBER_OF_BALLS= 10
    for i in range(NUMBER_OF_BALLS):
         x = random.randint(int(-SCREEN_WIDTH) + MAXIMUM_BALL_RADIUS ,int(SCREEN_WIDTH)- MAXIMUM_BALL_RADIUS)
         y = SCREEN_HEIGHT
         dy =random.randint(MINIMUM_BALL_Dy, MAXIMUM_BALL_Dy)
         radius =random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
         color =(random.random(),random.random(),random.random())
         New_Asteroids = Asteroids(x,y,dy,radius, color)
         ASTEROIDS.append(New_Asteroids)
         turtle.update()
         
CREATEBALLS()


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
arrow_circle.showturtle()

print(arrow_circle.shapesize())

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

        while True:
            for i in ASTEROIDS:
                i.MoveDown()
                 
                if(i.ycor() == -SCREEN_HEIGHT):
                    i.goto(i.x,SCREEN_HEIGHT)

        
                
        
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
    #red_laser.hideturtle()
    arrow.goto(space.xcor() - 5, space.ycor() + 15)
    arrow_circle.goto(arrow.xcor(), arrow.ycor())
    arrow.showturtle()
    arrow.penup()
    arrow.color("lightblue")
    turtle.penup()
    size = 10
    # print("size: " + str(size))
    while arrow.ycor() + size < SCREEN_HEIGHT:
        current_y = arrow.ycor()
        new_y = arrow.ycor() + 0.25
        # arrow.goto(arrow.xcor(), new_y)
        arrow_circle.goto(arrow.xcor() + 5, arrow.ycor() + size)
        moving_t.forward(15)
        arrow.hieght = size
        # print(arrow.hieght)
        # print("size: " + str(size))
        turtle.register_shape("rec", ((0, 0), (arrow.width, 0), (arrow.width, arrow.hieght), (0, arrow.hieght), (0, 0)))
        arrow.shape("rec")
        size += 5
        for astroid in ASTEROIDS:
            check_astroid_collision(astroid)
            astroid.MoveDown()
            
            
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

