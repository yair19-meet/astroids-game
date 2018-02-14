from turtle import Turtle
class Asteroids(Turtle):
    def __init__(self,x,y,dy,r,color):
        Turtle.__init__(self)
        self.penup()
        self.goto(x, y)
        self.dy = dy
	self.x = x
        self.r = r
        self.color(color)
        self.shape("circle")

    def move():
        current_y = self.ycor()
        new_y = current_y + self.dy
        down_side_asteroids = new_y - self.r            
        if(down_side_asteroids == -SCREEN_HEIGHT):
          self.goto(self.x,SCREEN_HEIGHT)

        self.goto(new_x,new_y)


SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
ASTEROIDS[]

for i in range(NUMBER_OF_BALLS):
     x = random.randint(int(-SCREEN_WIDTH) + MAXIMUM_BALL_RADIUS ,int(SCREEN_WIDTH)- MAXIMUM_BALL_RADIUS)
     y = screen_height
     dy =random.randint(MINIMUM_BALL_Dy, MAXIMUM_BALL_Dy)
     radius =random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
     color =(random.random(),random.random(),random.random())
     New_Asteroids = Asteroids(x,y,dy,radius, color)
     ASTEROIDS.append(new_asteroid) 
