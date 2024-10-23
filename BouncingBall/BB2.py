import pygame
from pygame import mixer
import time
from math import *

pygame.init()

screen = pygame.display.set_mode((800, 600))

KE = 5*600

class Ball:
    def __init__(self, x, y, xmov, ymov):
        self.x = x
        self.y = y
        self.xmov = xmov
        self.ymov = ymov

    def move(self):
        self.x += self.xmov
        self.y += self.ymov

    def draw(self):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), 10)

RUN = True

ball = Ball(400, 30, 0, 2) # Change Speed Here

h = []


dir = 1

while RUN:
    
    time.sleep(1/30)
    

    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
                
    ball.h = 590 - ball.y

    if ball.h >= 580:
        dir = 1
        
    if ball.h <= 0:
        dir = -1
        
    print(ball.h)
    h.append(ball.h)
    
    
    
    ball.ymov = sqrt(2.5*(ball.y))*dir
    
    ball.draw()
    ball.move()
    
    
    
    pygame.display.update()
    
print(min(h))
print(max(h))