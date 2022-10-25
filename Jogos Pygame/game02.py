import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

larg = 640
alt = 480

x = larg / 2 - 10
y = alt / 2 - 10
yVel = 0

x2 = randint(0, larg - 20)
y2 = randint(0, alt - 20)

pontos = 0

tela = pygame.display.set_mode((larg, alt))
pygame.display.set_caption('Game02')
fonte = pygame.font.SysFont('gabriola', 40, False, False)

rel = pygame.time.Clock()


def atualizar():
    global y, x, pontos, x2, y2
    
    q1 = pygame.draw.rect(tela, (255, 0, 0), (x, y, 20, 20))
    q2 = pygame.draw.rect(tela, (0, 0, 255), (x2, y2, 20, 20))

    if q1.colliderect(q2):
        x2 = randint(0, larg - 20)
        y2 = randint(0, alt - 20)
        pontos += 1

    keys = pygame.key.get_pressed()

    if keys[K_UP]:
        y -= 1

    if keys[K_DOWN]:
        y += 1

    if keys[K_RIGHT]:
        x += 1

    if keys[K_LEFT]:
        x -= 1


while True:
    tela.fill((0, 0, 0))

    text = f'Pontos: {pontos}'
    formated = fonte.render(text, False, (255, 255, 255))

    rel.tick(100)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    atualizar()

    tela.blit(formated, (450, 40))
    pygame.display.update()
