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


class Game:
    def __init__(self, window):
        self.balls = list()
        self.balls.append(Ball(window))

    def input(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.balls.append(Ball(window))

    def game_graphics(self):
        pygame.draw.rect(window, (0, 0, 0), (0, 0, 800, 600))
        mousepos = pygame.mouse.get_pos()
        pygame.draw.rect(window, (0, 0, 255), (mousepos[0], 550, 80, 20))
        self.ball_movement(mousepos)
        pygame.display.update()

    def ball_movement(self, mousepos):
        for ball in self.balls:
            if (ball.x > 800 or ball.x < 0): ball.vel_x *= -1
            if (ball.x > mousepos[0]) and (ball.x < mousepos[0] + 80) and (
                    ball.y == 550): ball.vel_y *= -1
            if (ball.y < 0): ball.vel_y *= -1
            if (ball.y > 600):
                ball.x = randint(0, 500)
                ball.y = randint(0, 100)
            ball.x += ball.vel_x
            ball.y  += ball.vel_y
            pygame.draw.circle(window, (255, 255, 255), (ball.x, ball.y), 6)


    def play(self):
        while True:
            self.input(pygame.event.get())
            self.game_graphics()


game = Game(window)
game.play()