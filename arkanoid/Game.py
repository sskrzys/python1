import pygame, sys, os
from random import randint

pygame.init()
window = pygame.display.set_mode((800, 600))


class Ball:
    def __init__(self, window):
        self.x = randint(0, 500)
        self.y = randint(0, 100)
        self.vel_x = 1
        self.vel_y = 1
        self.window = window

class Brick:
    def __init__(self, window, x, y):
        self.x = randint(0, 750)
        self.y = randint(0, 500)
        self.colorR = randint(0, 255)
        self.colorG = randint(0, 255)
        self.colorB = randint(0, 255)
        self.window = window

class Game:
    def __init__(self, window):
        self.balls = list()
        self.bricks = list()
        self.bricks.append(Brick(window, 500, 50))
        self.balls.append(Ball(window))

    def input(self, events):
        key = pygame.key.get_pressed()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.balls.append(Ball(window))
            if key[pygame.K_1]:
                self.bricks.append(Brick(window, 200, 200))

    def game_graphics(self):
        pygame.draw.rect(window, (0, 0, 0), (0, 0, 800, 600))
        mousepos = pygame.mouse.get_pos()
        pygame.draw.rect(window, (0, 0, 255), (mousepos[0], 550, 80, 20))
        self.bricks_present()
        self.ball_movement(mousepos)
        myfont = pygame.font.SysFont("monospace", 15)
        label_balls = myfont.render("Balls: " + str(self.balls.__len__()), 1, (0, 255, 0))
        label_bricks = myfont.render("Bricks: " + str(self.bricks.__len__()), 1, (255, 255, 0))
        label_info = myfont.render("1 on keyboar = brick, leftclick = ball", 1, (255, 0, 0))
        window.blit(label_balls, (0, 0))
        window.blit(label_bricks, (0, 25))
        window.blit(label_info, (0,50))
        pygame.display.update()
        pygame.time.wait(1)

    def ball_movement(self, mousepos):
        for ball in self.balls:
            if (ball.y > 600):
                self.balls.pop(self.balls.index(ball))
            if (ball.x > 800 or ball.x < 0): ball.vel_x *= -1
            if (ball.x > mousepos[0]) and (ball.x < mousepos[0] + 80) and (ball.y == 550):
                ball.vel_y *= -1
            if ball.y < 0:
                ball.vel_y *= -1
            ball.x += ball.vel_x
            ball.y += ball.vel_y
            pygame.draw.circle(window, (255, 255, 255), (ball.x, ball.y), 6)
        if self.balls.__len__() > 0:
            for brick in self.bricks:
                if(ball.x + 6 > brick.x) and (ball.x + 6 < brick.x + 50) and (ball.y + 6 > brick.y) and (ball.y + 6 < brick.y + 25):
                    if ball.y > brick.y and brick.x < ball.x < brick.x + 50:
                        ball.vel_y *= -1
                    if ball.y < brick.y and brick.x < ball.x < brick.x + 50:
                        ball.vel_y *= -1
                    if ball.x > brick.x and brick.y < ball.y < brick.y + 50:
                        ball.vel_x *= -1
                    if ball.x < brick.x and brick.y < ball.y < brick.y + 50:
                        ball.vel_x *= -1
                    self.bricks.pop(self.bricks.index(brick))
    def bricks_present(self):
        for brick in self.bricks:
            pygame.draw.rect(window, (brick.colorR, brick.colorG, brick.colorB), (brick.x, brick.y, 50, 25))


    def play(self):
        clear = lambda : os.system('cls')
        while True:
            self.input(pygame.event.get())
            self.game_graphics()
            pygame.event.pump()


game = Game(window)
game.play()