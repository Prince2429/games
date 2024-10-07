import turtle as tr
import winsound as os
wn = tr.Screen()
wn.title("Air Hockey by Pranav")
wn.bgcolor("yellow")
wn.setup(width=800, height=600)  # Sets the size of the screen
wn.tracer(0)  # Turns off the animation delay

#score
score_a=0
score_b=0
#paddle a
paddle_a = tr.Turtle()
paddle_a.speed(0)  # Speed of 0 is the fastest speed
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle b
paddle_b = tr.Turtle()
paddle_b.speed(0)  # Speed of 0 is the fastest speed
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#ball
ball = tr.Turtle()
ball.speed(0)  # Speed of 0 is the fastest speed
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0,0)
ball.dx=0.07
ball.dy=0.07

#pen
pen=tr.Turtle()
pen.speed(0)
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("John:0   Don:0",align=("center"),font=("Courier",24,"bold"))


#function
def  paddle_a_up():
    y=paddle_a.ycor()
    if y<240:
     y+=20
     paddle_a.sety(y)

def  paddle_a_down():
    y=paddle_a.ycor()
    if y>-240:
     y-=20
     paddle_a.sety(y)    

def  paddle_b_up():
    y=paddle_b.ycor()
    if y<240:
     y+=20
     paddle_b.sety(y)

def  paddle_b_down():
    y=paddle_b.ycor()
    if y>-240:
     y-=20
     paddle_b.sety(y)  
#keyboard listening
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

    
# Loop

while True:
    wn.update()  # Updates the display to

    #move ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy*=-1
        os.PlaySound("bounce.wav",os.SND_ASYNC)
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy*=-1 
        os.PlaySound("bounce.wav",os.SND_ASYNC)
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx*=-1
        score_b+=1
        pen.clear()
        pen.write("John:{}   Don:{}".format(score_a,score_b),align=("center"),font=("Courier",24,"bold"))
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx*=-1  
        score_a+=1 
        pen.clear() 
        pen.write("John:{}   Don:{}".format(score_a,score_b),align=("center"),font=("Courier",24,"bold"))
    #paddle and ball collision
    if ball.xcor() > 340 and ball.xcor()<350 and (ball.ycor() < paddle_b.ycor()+40 and ball.ycor() > paddle_b.ycor()-40):
        ball.dx*=-1
        os.PlaySound("bounce.wav",os.SND_ASYNC)
    if ball.xcor() < -340 and ball.xcor()>-350 and (ball.ycor() < paddle_a.ycor()+40 and ball.ycor() > paddle_a.ycor()-40):
        ball.dx*=-1 
        os.PlaySound("bounce.wav",os.SND_ASYNC)    





