import pygame, sys, os
from pygame.locals import *

pygame.init()
# utworzenie okna
window = pygame.display.set_mode((800, 600))
# ustawiamy etykietę
pygame.display.set_caption('Krzyśkanoid')
WHITE = (255,255,255)
blue=(0,0,255)
black = (0,0,0)

def ball(x,y):
    pygame.draw.circle(window, WHITE, (x, y), 6)


def input(events):
    ballmovx = 200
    ballmovy = 300
    for event in events:
        if event.type == QUIT:
            sys.exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("edlo")
            pygame.draw.rect(window, WHITE, (50, 50, 40, 20))
            ballmovx += 222
        if event.type == pygame.event.pump():
            ballmovx += 2

        pygame.draw.rect(window, black, (0,0,800,600))
        mousepos = pygame.mouse.get_pos()
        ballmovx += 222
        pygame.draw.rect(window, blue, (mousepos[0], 550, 80, 20))  # padzik pod spodem dziala dobrze juz
        ball(ballmovx,ballmovy)  # sluzy rysowaniu pilkibala
        pygame.display.update()


# działaj aż do przerwania
while True:
    input(pygame.event.get())
