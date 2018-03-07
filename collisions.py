def collide(arrow_circle, astroid):
	D = math.sqrt(math.pow(arrow_circle.xcor()-astroid.xcor(), 2) + math.pow(arrow_circle.ycor()-astroid.ycor(),2))
	sum_r= (arrow_circle.shapesize()/10)+astroid.r
	if(D+10<=sum_r):
        return True
    return False


def check_astroid_collision():
	if collide(arrow_circle,astroid)==True: 
            X=random.randint(round(-SCREEN_WIDTH)+MAXIMUM_BALL_RADIUS, round(SCREEN_WIDTH) - MAXIMUM_BALL_RADIUS)
            Y= random.randint(SCREEN_HIGHT,SCREEN_HIGHT+80)
            astroid.goto(X,Y)