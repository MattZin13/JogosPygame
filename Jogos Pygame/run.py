import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

larg = 640
alt = 480
zx = larg / 2
zy = alt / 2
extime = 0
time = 0

tela = pygame.display.set_mode((larg, alt))
pygame.display.set_caption('Run!')

tamPlayer = 30
xPlayer = zx +50 + tamPlayer / 2
yPlayer = zy - tamPlayer / 2
velPlay = 1.2

xEnemy1 = 30
yEnemy1 = zy +20
xVel1 = 1.8
yVel1 = 1.8
tamEnemy1 = 15

xEnemy2 = 30
yEnemy2 = zy -20
xVel2 = 0.9
yVel2 = 0.9
tamEnemy2 = 45

tamCrystal = 15
xCrystal = randint(0, larg - tamCrystal)
yCrystal = randint(0, alt - tamCrystal)

rel = pygame.time.Clock()

def atualizar():
    global yPlayer, xPlayer, xEnemy1, yEnemy1, xEnemy2, yEnemy2, xVel1, yVel1, xVel2, yVel2, time, extime, xCrystal, yCrystal, velPlay

    xEnemy1 += xVel1
    yEnemy1 += yVel1
    xEnemy2 += xVel2
    yEnemy2 += -yVel2
    time += 1

    player = pygame.draw.rect(tela, (255, 255, 255), (xPlayer, yPlayer, tamPlayer, tamPlayer))
    enemy1 = pygame.draw.rect(tela, (0, 0, 255), (xEnemy1, yEnemy1, tamEnemy1, tamEnemy1))
    enemy2 = pygame.draw.rect(tela, (255, 0, 0), (xEnemy2, yEnemy2, tamEnemy2, tamEnemy2))
    crystal = pygame.draw.rect(tela, (0, 255, 0), (xCrystal, yCrystal, tamCrystal, tamCrystal))

    if player.colliderect(enemy1) or player.colliderect(enemy2):
        xPlayer = zx +50 + tamPlayer / 2
        yPlayer = zy - tamPlayer / 2
        xEnemy1 = 30
        yEnemy1 = zy +20
        xEnemy2 = 30
        yEnemy2 = zy -20
        xVel1 = yVel1 = velPlay = 1.2
        xVel2 = yVel2 = 1

    if player.colliderect(crystal):
        xCrystal = randint(0, larg - tamCrystal)
        yCrystal = randint(0, alt - tamCrystal)
        if xVel1 > 0:
            xVel1 += 0.1
        elif xVel1 < 0:
            xVel1 -= 0.1

        if yVel1 > 0:
            yVel1 += 0.1
        elif yVel1 < 0:
            yVel1 -= 0.1

        if xVel2 > 0:
            xVel2 += 0.1
        elif xVel2 < 0:
            xVel2 -= 0.1

        if yVel2 > 0:
            yVel2 += 0.1
        elif yVel2 < 0:
            yVel2 -= 0.1

        velPlay += 0.1

    if yEnemy1 < 0:
        yVel1 = -yVel1

    if yEnemy1 + tamEnemy1 > alt:
        yVel1 = -yVel1

    if xEnemy1 < 0:
        xVel1 = -xVel1

    if xEnemy1 + tamEnemy1 > larg:
        xVel1 = -xVel1

    if yEnemy2 < 0:
        yVel2 = -yVel2

    if yEnemy2 + tamEnemy2 > alt:
        yVel2 = -yVel2

    if xEnemy2 < 0:
        xVel2 = -xVel2

    if xEnemy2 + tamEnemy2 > larg:
        xVel2 = -xVel2


    keys = pygame.key.get_pressed()

    if yPlayer + tamPlayer < alt:
        if keys[K_DOWN]:
            yPlayer += velPlay

    if yPlayer > 0:
        if keys[K_UP]:
            yPlayer -= velPlay

    if xPlayer > 0:
        if keys[K_LEFT]:
            xPlayer -= velPlay

    if xPlayer + tamPlayer < larg:
        if keys[K_RIGHT]:
            xPlayer += velPlay

    if time - extime == 4000:
        extime = time
        if xVel1 <= 3.2:
            if xVel1 < 0:
                xVel1 -= 0.1
            elif xVel1 > 0:
                xVel1 += 0.1      
        if yVel1 <= 3.2:      
            if yVel1 < 0:
                yVel1 -= 0.1
            elif yVel1 > 0:
                yVel1 += 0.1
        if xVel2 <= 3:
            if xVel2 < 0:
                xVel2 -= 0.1
            elif xVel2 > 0:
                xVel2 += 0.1
        if xVel2 <= 3:
            if yVel2 < 0:
                yVel2 -= 0.1
            elif yVel2 > 0:
                yVel2 += 0.1


while True:
    tela.fill((0, 0, 0))

    rel.tick(100)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    atualizar()

    pygame.display.update()
