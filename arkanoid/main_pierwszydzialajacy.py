import pygame, sys, os
from random import randint
from pygame.locals import *

pygame.init()
# utworzenie okna
window = pygame.display.set_mode((800, 600))
# ustawiamy etykietę
pygame.display.set_caption('Krzyśkanoid')

ballmovx = randint(0,500)
ballmovy = randint(0,100)

velocity_x = 1
velocity_y = 1

done = False

def ball(x,y):
    pygame.draw.circle(window, (255,255,255), (x, y), 6)


def input(events):
    for event in events:
        if event.type == QUIT:
            sys.exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("edlo")

# działaj aż do przerwania
while not done:
    input(pygame.event.get())
    pygame.draw.rect(window, (0,0,0), (0, 0, 800, 600))
    mousepos = pygame.mouse.get_pos()  # pobieramy pozycje kursora ziom
    ballmovx += velocity_x  # poruszamy pilka
    if (ballmovx > 800) or (ballmovx < 0): velocity_x *= -1
    ballmovy += velocity_y
    if (ballmovx > mousepos[0]) and (ballmovx < mousepos[0] + 80) and (ballmovy == 550): velocity_y *= -1
    if (ballmovy < 0): velocity_y *= -1
    if (ballmovy > 600):
        ballmovx = randint(0, 500)
        ballmovy = randint(0, 100)
    pygame.draw.rect(window, (0,0,255), (mousepos[0], 550, 80, 20))  # padzik pod spodem dziala dobrze juz
    ball(ballmovx, ballmovy)  # sluzy rysowaniu pilkibala
    pygame.display.update()  # no rysujemy rzeczy
    pygame.time.wait(1)  # no czekamy zeby nie bylo za szybko