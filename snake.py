import turtle as tr
import time as t
import random as ran

delay = 0.1

#score
score=0
high_score=0
wn = tr.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)  # Set up the screen
wn.tracer(0)  # Turn off animation

#snake head
head = tr.Turtle()
head.speed(0)
head.shape("circle")
head.color("yellow")
head.shapesize(1.1)
head.penup()
head.goto(0,0)
head.penup()
head.direction= "stop"

segments = []

#pen
pen =tr.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score:0  HighScore=0", align="center", font=("Courier",24,"bold"))
#snake food
food = tr.Turtle()
food.speed(0)
food.shape("circle")
food.shapesize(0.6)
food.color("red")
food.penup()
food.goto(0,200)

#functions
def go_up():
   if head.direction!="down": 
    head.direction = "up"
    
def go_down():
   if head.direction!="up": 
    head.direction = "down"
        
def go_left():
   if head.direction!="right": 
    head.direction = "left"
    
def go_right():
   if head.direction!="left": 
    head.direction = "right"

#keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

def move():
    if head.direction == "up":
        y = head.ycor() + 20
        head.sety(y)
    elif head.direction == "down":
        y = head.ycor() - 20
        head.sety(y)
    elif head.direction == "right":
        x = head.xcor() + 20
        head.setx(x)
    else:
        x = head.xcor() - 20
        head.setx(x)

#main loop
while True:
    wn.update()

    #collision
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        t.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

    #hide segments
        for segment in segments:
            segment.goto(5000,5000)
        segments.clear()
        #reset
        delay=0.1
        score=0
        pen.clear()   
        pen.write("Score:{} HighScore:{}".format(score,high_score),align="center",font=("Courier",24,"bold")) 
            
    if head.distance(food) <  20:
        x = ran.randint(-290,290)
        y= ran.randint(-290,290)
        food.goto(x,y)
        new_segment  = tr.Turtle()
        new_segment.speed(0)
        new_segment.color("green")
        new_segment.shape("circle")
        new_segment.penup()
        segments.append(new_segment)
        #delay decrease
        delay -= 0.001
        #increase score
        score+=10

        if score>high_score:
           high_score=score
        pen.clear()   
        pen.write("Score:{} HighScore:{}".format(score,high_score),align="center",font=("Courier",24,"bold"))   
    

    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    if(len(segments)>0):
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
    move()    
#head collision
    for segment in segments:
        if segment.distance(head)<20:
            t.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            for segment in segments:
              segment.goto(5000,5000)
            segments.clear()
            #reset delay and score
            delay=0.1
            score=0
            pen.clear()   
            pen.write("Score:{} HighScore:{}".format(score,high_score),align="center",font=("Courier",24,"bold")) 
    t.sleep(delay)
wn.mainloop()    
