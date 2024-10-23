import turtle
from math import *
import time

theta = -radians(int(input("Enter angle: ")))
angle = theta

windowHeight = 800
windowWidth = 800

window = turtle.Screen()
window.title("Pendulum")
window.bgcolor("white")
window.setup(windowWidth, windowHeight)
window.tracer(0)

ball = turtle.Turtle()
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(400*sin(angle),400-400*cos(angle))

gravity = -19.6
drag = 0.008

xspeed = 0
yspeed = 0

while True:
    time.sleep(1/120)
    
    turtle.clear()
    
    height = windowHeight/2 - ball.ycor()
    deviation = ball.xcor()
    
    angle = asin(deviation/400)
    
    ball.sety(400 - sqrt(160000 - deviation**2))
    
    xacc = gravity * sin(angle) * cos(angle)
    
    xspeed += xacc/30
    
    if xspeed < 0:
        xspeed += drag
    else:
        xspeed -= drag
    
    ball.setx(ball.xcor() + xspeed)    
    
    turtle.penup()
    turtle.goto(0,400)
    turtle.pendown()
    turtle.goto(ball.xcor(), ball.ycor())
    turtle.hideturtle()    
    
    print(ball.pos(), degrees(angle),"\n",  height)
    print(sqrt(ball.xcor()**2 + (400-ball.ycor())**2))
    
    window.update()