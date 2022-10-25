import pygame
from pygame.locals import *
from OpenGL.GL import *

larg_jan = 640
alt_jan = 480

yPlayer = 0
xPlayer = 0
tamPlayer = 20
vidaPlayer = 3

tamEnemies = tamPlayer
xEnemy1 = -larg_jan / 2 + tamEnemies / 2
yEnemy1 = -20
velEnemy1X = 0.2
velEnemy1Y = 0.2

xEnemy2 = -larg_jan / 2 + tamEnemies / 2
yEnemy2 = 20
velEnemy2X = 0.2
velEnemy2Y = 0.2

def atualizar():
    global xPlayer, yPlayer, xEnemy1, xEnemy2, velEnemy1X, velEnemy1Y, velEnemy2X, velEnemy2Y, yEnemy1, yEnemy2

    xEnemy1 = xEnemy1 + velEnemy1X
    xEnemy2 = xEnemy2 + velEnemy2X
    yEnemy1 = yEnemy1 - 0.2
    yEnemy2 = yEnemy2 + 0.2

    if xEnemy1 + tamEnemies / 2 > larg_jan / 2:
        velEnemy1X = -velEnemy1X


    if xEnemy2 + tamEnemies / 2 > larg_jan / 2:
        velEnemy2X = -velEnemy2X
    

    if xEnemy1 - tamEnemies / 2 < -larg_jan / 2:
        velEnemy1X = -velEnemy1X


    if xEnemy2 - tamEnemies / 2 < -larg_jan / 2:
        velEnemy2X = -velEnemy2X
    

    if yEnemy1 + tamEnemies / 2 > alt_jan / 2:
        velEnemy1Y = -velEnemy1Y


    if yEnemy2 + tamEnemies / 2 < alt_jan / 2:
        velEnemy2Y = -velEnemy2Y
    

    if yEnemy1 - tamEnemies / 2 > -alt_jan / 2:
        velEnemy1Y = -velEnemy1Y


    if yEnemy2 - tamEnemies / 2 < -alt_jan / 2:
        velEnemy2Y = -velEnemy2Y


    # Parte de cima Player

    # if (yEnemy1 - tamEnemies / 2 < yPlayer + tamPlayer / 2
    # and xEnemy1 - tamEnemies / 2 < xPlayer + tamPlayer / 2   # Enemy 1
    # and xEnemy1 + tamEnemies / 2 > xPlayer - tamPlayer / 2):
    #     xEnemy1 = -larg_jan / 2 + tamEnemies / 2
    #     yEnemy1 = -20

    
    # if (yEnemy2 - tamEnemies / 2 < yPlayer + tamPlayer / 2
    # and xEnemy2 - tamEnemies / 2 < xPlayer + tamPlayer / 2  # Enemy 2
    # and xEnemy2 + tamEnemies / 2 > xPlayer - tamPlayer / 2):
    #     xEnemy2 = -larg_jan / 2 + tamEnemies / 2
    #     yEnemy2 = 20

    # Parte de baixo Player

    # if (yEnemy1 + tamEnemies / 2 > yPlayer - tamPlayer / 2
    # and xEnemy1 - tamEnemies/ 2 < xPlayer + tamPlayer / 2   # Enemy 1
    # and xEnemy1 + tamEnemies/ 2 > xPlayer - tamPlayer / 2):
    #     xEnemy1 = -larg_jan / 2 + tamEnemies / 2
    #     yEnemy1 = -20

    # if (yEnemy2 + tamEnemies / 2 > yPlayer - tamPlayer / 2
    # and xEnemy2 - tamEnemies / 2 < xPlayer + tamPlayer / 2   # Enemy 2
    # and xEnemy2 + tamEnemies / 2 > xPlayer - tamPlayer / 2):
    #     xEnemy2 = -larg_jan / 2 + tamEnemies / 2
    #     yEnemy2 = 20

    # Direita Player

    # if (xEnemy1 - tamEnemies / 2 < xPlayer + tamPlayer / 2
    # and yEnemy1 - tamEnemies / 2 < yPlayer + tamPlayer / 2   # Enemy 1
    # and yEnemy1 + tamEnemies / 2 > yPlayer - tamPlayer / 2):
    #     xEnemy1 = -larg_jan / 2 + tamEnemies / 2
    #     yEnemy1 = -20

    # if (xEnemy2 - tamEnemies / 2 < xPlayer + tamPlayer / 2
    # and yEnemy2 - tamEnemies / 2 < yPlayer + tamPlayer / 2   # Enemy 2
    # and yEnemy2 + tamEnemies / 2 > yPlayer - tamPlayer / 2):
    #     xEnemy2 = -larg_jan / 2 + tamEnemies / 2
    #     yEnemy2 = 20

    # # Esquerda Player

    # if (xEnemy1 + tamEnemies / 2 > xPlayer - tamPlayer / 2
    # and yEnemy1 - tamEnemies / 2 < yPlayer + tamPlayer / 2   # Enemy 1
    # and yEnemy1 + tamEnemies / 2 > yPlayer - tamPlayer / 2):
    #     xEnemy1 = -larg_jan / 2 + tamEnemies / 2
    #     yEnemy1 = -20

    # if (xEnemy2 + tamEnemies / 2 > xPlayer - tamPlayer / 2
    # and yEnemy2 - tamEnemies / 2 < yPlayer + tamPlayer / 2   # Enemy 2
    # and yEnemy2 + tamEnemies / 2 > yPlayer - tamPlayer / 2):
    #     xEnemy2 = -larg_jan / 2 + tamEnemies / 2
    #     yEnemy2 = 20

    # if retPlayer.colliderect(retEnemy1):
    #     xEnemy1 = -larg_jan / 2 + tamEnemies / 2
    #     yEnemy1 = -20

    # if retPlayer.colliderect(retEnemy2):
    #     xEnemy2 = -larg_jan / 2 + tamEnemies / 2
    #     yEnemy2 = 20
    
    keys = pygame.key.get_pressed()

    if keys[K_UP]:
        yPlayer = yPlayer + 0.3

    if keys[K_DOWN]:
        yPlayer = yPlayer - 0.3

    if keys[K_RIGHT]:
        xPlayer = xPlayer + 0.3
    
    if keys[K_LEFT]:
        xPlayer = xPlayer - 0.3


# def desenharRetangulo(x, y, larg, alt, r, g, b):
#     glColor3f(r, g, b)

#     glBegin(GL_QUADS)
#     glVertex2f(-0.5 * larg + x, -0.5 * alt + y)
#     glVertex2f(0.5 * larg + x, -0.5 * alt + y)
#     glVertex2f(0.5 * larg + x, 0.5 * alt + y)
#     glVertex2f(-0.5 * larg + x, 0.5 * alt + y)
#     glEnd()

# def desenhar():
#     glViewport(0, 0, larg_jan, alt_jan)

#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     glOrtho(-larg_jan / 2, larg_jan / 2, -alt_jan / 2, alt_jan / 2, 0, 1)

#     glClear(GL_COLOR_BUFFER_BIT)

#     # desenharRetangulo(xEnemy1, yEnemy1, tamEnemies, tamEnemies, 1, 0, 0)
#     # desenharRetangulo(xEnemy2, yEnemy2, tamEnemies, tamEnemies, 0, 0, 1)
#     # desenharRetangulo(xPlayer, yPlayer, tamPlayer, tamPlayer, 0, 1, 0)

#     retPlayer
#     retEnemy1
#     retEnemy2

#     pygame.display.flip() 

pygame.init()
tela = pygame.display.set_mode((larg_jan, alt_jan), DOUBLEBUF | OPENGL)

pygame.draw.rect(tela, (0, 255, 0), (xPlayer, yPlayer, tamPlayer, tamPlayer))
pygame.draw.rect(tela, (255, 0, 0), (xEnemy1, yEnemy1, tamEnemies, tamEnemies))
pygame.draw.rect(tela, (0, 0, 255), (xEnemy2, yEnemy2, tamEnemies, tamEnemies))

while True:
    atualizar()
    # desenhar()
    # retPlayer
    # retEnemy1
    # retEnemy2
    pygame.event.pump()
