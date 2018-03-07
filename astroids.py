from turtle import Turtle
import turtle
import random
turtle.tracer(0)
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

    def move(self):
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
       self.forward(-2)
       turtle.update()

RUNNING = True
      
MAXIMUM_BALL_RADIUS = 20
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_Dy = 5
MINIMUM_BALL_Dy = 3
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
ASTEROIDS=[]

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

#ASTEROIDS[0].MoveDown()
while RUNNING == True:
    for i in ASTEROIDS:
       i.MoveDown()


