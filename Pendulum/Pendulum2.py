import turtle
from math import *
import time

theta = -radians(int(input("Enter angle: ")))
length=int(input('Enter length of string(400): '))
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

gravity = 9.8

init_time = time.time()

while True:
    time.sleep(1/120)
    
    turtle.clear()
    
    t=int(time.time()-init_time)
    angle=asin(abs(ball.xcor())/length)
    
    ball_x=length*sin(angle)*cos(sqrt(2.5*length*gravity*(1-cos(angle)))*t)
    ball.setx(ball_x)
    
    turtle.penup()
    turtle.goto(0,length)
    turtle.pendown()
    turtle.goto(ball.xcor, ball.ycor())
    turtle.hideturtle()    
    
    # print(ball.pos(), degrees(angle),"\n",  height)
    # print(sqrt(ball.xcor()**2 + (400-ball.ycor())**2))
    
    window.update()