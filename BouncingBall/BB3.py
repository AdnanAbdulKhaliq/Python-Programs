import turtle
import time
from math import *


speed = float(input("Enter the speed of the ball: "))

wn = turtle.Screen()
wn.title("BouncingBall")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,285)

exit = False

def exit_fn():
    global exit
    exit = True

wn.listen()


gravity = -1
drag = 0.00001
speedLoss = 0.8

t = 0
sign = 1

sign2 = 1

while True:
    time.sleep(1/120)
    
    wn.update()
    
    speed += gravity
    if speed > 0:
        speed += speed**2 * 0.0002
    else:
        speed -= speed **2 * 0.0002
        
    if ball.ycor() > 300:
        speed = -speed * speedLoss
        ball.sety(300)
    if ball.ycor() < -290:
        speed = -speed * speedLoss
        ball.sety(-290)
            
    
    ball.sety(ball.ycor() + (speed*sign))
    
    
    print(ball.ycor())