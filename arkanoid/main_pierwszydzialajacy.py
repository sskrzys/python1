import pygame, sys, os
from random import randint
from pygame.locals import *

pygame.init()
# utworzenie okna
window = pygame.display.set_mode((800, 600))
# ustawiamy etykietę
pygame.display.set_caption('Krzyśkanoid')




def ball(x,y):
    print("edlo")
    pygame.draw.circle(window, (255,255,255), (x, y), 6)

def input(events):
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
            #

class Ball:
    def __init__(self):
        self.ballmovx = randint(0, 500)
        self.ballmovy = randint(0, 100)
        self.velocity_x = 1
        self.velocity_y = 1

    def baller(self):
        self.ballmovx += self.velocity_x  # poruszamy pilka
        self.ballmovy += self.velocity_y

        if (self.ballmovx > 800) or (self.ballmovx < 0): self.velocity_x *= -1
        if (self.ballmovx > mousepos[0]) and (self.ballmovx < mousepos[0] + 80) and (self.ballmovy == 550): self.velocity_y *= -1
        if (self.ballmovy < 0): self.velocity_y *= -1
        if (self.ballmovy > 600):
            self.ballmovx = randint(0, 500)
            self.ballmovy = randint(0, 100)
        pygame.draw.rect(window, (0, 0, 255), (mousepos[0], 550, 80, 20))  # padzik pod spodem dziala dobrze juz
        #ball(ballmovx, ballmovy)  # sluzy rysowaniu pilkibala
        pygame.draw.circle(window, (255, 255, 255), (self.ballmovx, self.ballmovy), 6)

# działaj aż do przerwania
ball = Ball()
ball1 = Ball()
while True:
    input(pygame.event.get())
    pygame.draw.rect(window, (0,0,0), (0, 0, 800, 600))
    mousepos = pygame.mouse.get_pos()  # pobieramy pozycje kursora ziom
    ball.baller()
    ball1.baller()

    pygame.display.update()  # no rysujemy rzeczy
    #pygame.time.wait(1)  # no czekamy zeby nie bylo za szybko
