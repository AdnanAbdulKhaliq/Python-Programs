import turtle
import time
from math import *


wn = turtle.Screen()
wn.title("BouncingBall")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,285)

exit = False

def exit_fn():
    global exit
    exit = True

wn.listen()
wn.onkeypress(exit_fn, "h")

ball.speed = -5

sign = 1

while True:
    time.sleep(1/60)
    
    wn.update()
       
    
    
    if ball.ycor() <= -320:
        sign = 1

    if ball.ycor() > 285:
        sign = -1
       
    
    ball.speed = sqrt(300-ball.ycor())
       
    time.sleep(1/120)    
    ball.sety(ball.ycor() + (2*ball.speed*sign))
    print(ball.ycor())