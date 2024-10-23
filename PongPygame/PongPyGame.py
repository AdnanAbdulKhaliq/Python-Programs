# Pong Game
import pygame
from pygame import mixer
import time

# Initialising PyGame
pygame.init()

# Screen Variable
screen = pygame.display.set_mode((800, 600))

# Customizing Window Caption and Icon
pygame.display.set_caption("Ping Pong")
icon = pygame.image.load("PongPygame/Pong.png")
pygame.display.set_icon(icon)

# Colour Tuples
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Movement Variables
Player1_change = 0
Player2_change = 0

# Paddle Class
class Paddle:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def move(self, ymov):
        self.y += ymov

    def rect(self):
        paddle_rect = pygame.Rect(self.x, self.y, 10, 120)
        return paddle_rect

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect())

# Ball Class
class Ball:
    def __init__(self, x, y, xmov, ymov):
        self.x = x
        self.y = y
        self.xmov = xmov
        self.ymov = ymov

    def move(self):
        self.x += self.xmov
        self.y += self.ymov

    def rect(self):
        ball_rect = pygame.Rect(self.x-10, self.y-10, 20, 20)
        return ball_rect

    def draw(self):
        pygame.draw.rect(screen, BLACK, self.rect())
        pygame.draw.circle(screen, WHITE, (self.x, self.y), 10)

# Score Variables
Player1_points = 0
Player2_points = 0

# Paddle and Ball Objects
Player1 = Paddle(20, 240)
Player2 = Paddle(770, 240)
ball = Ball(400, 300, 3, 2) # Change Speed Here

#Loading Sound
Sound = mixer.Sound('PongPygame/bounce(1).wav')

RUN = True

while RUN:

    # Screen Refreshing Speed
    time.sleep(1/120)

    screen.fill((BLACK))

    # Exit Controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

    # Paddle Controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                Player1_change += -5

            if event.key == pygame.K_s:
                Player1_change += 5

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                Player2_change += -5

            if event.key == pygame.K_DOWN:
                Player2_change += 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                Player1_change = 0

            if event.key == pygame.K_s:
                Player1_change = 0

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                Player2_change = 0

            if event.key == pygame.K_DOWN:
                Player2_change = 0

    # Drawing
    Player1.move(Player1_change)
    Player2.move(Player2_change)

    Player1.draw()
    Player2.draw()
    ball.move()
    ball.draw()

    # Boundaries
    if Player1.y <= 0:
        Player1.y = 0

    elif Player1.y >= 480:
        Player1.y = 480

    if Player2.y <= 0:
        Player2.y = 0

    elif Player2.y >= 480:
        Player2.y = 480

    if ball.y <= 0:
        ball.ymov *= -1
        mixer.Sound.play(Sound)

    elif ball.y >= 590:
        ball.ymov *= -1
        mixer.Sound.play(Sound)

    # Paddle Collision Detection
    if ball.rect().colliderect(Player1.rect()):
        ball.xmov *= -1.
        mixer.Sound.play(Sound)

    if ball.rect().colliderect(Player2.rect()):
        ball.xmov *= -1.2
        mixer.Sound.play(Sound)

    # Point Detection
    if ball.x <= 10:
        Player2_points += 1
        ball.x = 400
        ball.y = 300
        ball.xmov = 3
        Player1.y = 240
        Player2.y = 240
        time.sleep(1/2)

    if ball.x >= 790:
        Player1_points += 1
        ball.x = 400
        ball.y = 300
        ball.xmov = -3
        Player1.y = 240
        Player2.y = 240
        time.sleep(1/2)

    # Text(Score) Rendering and Printing
    font = pygame.font.Font('freesansbold.ttf', 32)
    score = font. render(f'Player 1: {Player1_points}   Player 2: {Player2_points}', True, WHITE)
    screen.blit(score, (400 - score.get_rect().width/2, 10))

    # Updating the display
    pygame.display.update()