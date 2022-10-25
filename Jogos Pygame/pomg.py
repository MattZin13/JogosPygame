import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

larg = 640
alt = 480
zx = larg / 2

def posZY(z):
    return alt / 2 - z / 2

tela = pygame.display.set_mode((larg, alt))
pygame.display.set_caption(('Pimg-Pomg!'))

tamBall = 20
xBall = zx - tamBall
yBall = posZY(tamBall)
velBallY = 1.4
velBallX = 1.4

largPlayers = tamBall
altPlayers = 3 * tamBall
xPlayer1 = 0
yPlayer1 = posZY(altPlayers)

xPlayer2 = larg - largPlayers
yPlayer2 = posZY(altPlayers)

sinalX = randint(1, 2)
sinalY = randint(1, 2)
cont1 = 0
cont2 = 0

tab1 = ((0, 0, 255), (0, 0, 177), (0, 0, 99))
tab2 = ((255, 0, 0), (177, 0, 0), (99, 0, 0))

cor1 = tab1[0][:]
cor2 = tab2[0][:]

rel = pygame.time.Clock()

def atualizar():
    global xPlayer1, yPlayer1, xPlayer2, yPlayer2, xBall, yBall, cont1, cont2, velBallX, velBallY, cor1, cor2

    if sinalX == 1:
        xBall += -velBallX
    elif sinalX == 2:
        xBall += velBallX
    if sinalY == 1:
        yBall += -velBallY
    elif sinalY == 2:
        yBall += velBallY

    ball = pygame.draw.circle(tela, (180, 0, 255), (xBall, yBall), tamBall / 2 + 2)
    player1 = pygame.draw.rect(tela, (cor1[0], cor1[1], cor1[2]), (xPlayer1, yPlayer1, largPlayers, altPlayers))
    player2 = pygame.draw.rect(tela, (cor2[0], cor2[1], cor2[2]), (xPlayer2, yPlayer2, largPlayers, altPlayers))

    if ball.colliderect(player1) or ball.colliderect(player2):
        velBallX = -velBallX

    if yBall - tamBall / 2 < 0:
        velBallY = -velBallY
    if yBall + tamBall / 2 > alt:
        velBallY = -velBallY
    
    if xBall < 0:
        xBall = zx - tamBall
        yBall = posZY(tamBall)
        cont1 += 1
        if cont1 != 3:
            cor1 = tab1[cont1][:]

    if xBall + tamBall > larg:
        xBall = zx - tamBall
        yBall = posZY(tamBall)
        cont2 += 1
        if cont2 != 3:
            cor2 = tab2[cont2][:]

    if cont1 == 3 or cont2 == 3:
        yPlayer1 = posZY(altPlayers)
        yPlayer2 = posZY(altPlayers)
        velBallX = velBallY = 1.4
        cont1 = cont2 = 0
        cor1 = tab1[0][:]
        cor2 = tab2[0][:]

    keys = pygame.key.get_pressed()

    if yPlayer1 >= 0:
        if keys[K_w]:
            yPlayer1 -= 1.6
    if yPlayer1 + altPlayers <= alt:
        if keys[K_s]:
            yPlayer1 += 1.6
    
    if yPlayer2 >= 0:
        if keys[K_UP]:
            yPlayer2 -= 1.6
    if yPlayer2 + altPlayers <= alt:
        if keys[K_DOWN]:
            yPlayer2 += 1.6


while True:
    tela.fill((0, 0, 0))

    rel.tick(100)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    atualizar()
    
    pygame.display.update()
