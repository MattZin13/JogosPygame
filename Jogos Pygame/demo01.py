import pygame
from pygame.locals import *
from OpenGL.GL import *

larg_jan = 640
alt_jan = 480

yDaBola = 0
xDaBola = 0
tamDaBola = 20
velDaBolaY = 0.1
velDaBolaX = 0.1

altPlayer1 = 3 * tamDaBola
largPlayer1 = tamDaBola
xDoPlayer1 = -larg_jan / 2 + largPlayer1 / 2
yPlayer1 = 0


def atualizar():
    global xDaBola, yDaBola, velDaBolaX, velDaBolaY, yPlayer1, xDoPlayer1, largPlayer1, altPlayer1

    xDaBola = xDaBola + velDaBolaX
    yDaBola = yDaBola + velDaBolaY

    if (xDaBola + tamDaBola / 2 > xDoPlayer1 - largPlayer1 / 2 
    and yDaBola - tamDaBola / 2 < yPlayer1 + altPlayer1 / 2
    and yDaBola + tamDaBola / 2 > yPlayer1 - altPlayer1 / 2):
        velDaBolaX = -velDaBolaX

    if (xDaBola - tamDaBola / 2 < xDoPlayer1 + largPlayer1 / 2 
    and yDaBola - tamDaBola / 2 < yPlayer1 + altPlayer1 / 2
    and yDaBola + tamDaBola / 2 > yPlayer1 - altPlayer1 / 2):
        velDaBolaX = -velDaBolaX

    if (yDaBola + tamDaBola / 2 > yPlayer1 - largPlayer1 / 2
    and xDaBola - tamDaBola / 2 < xDoPlayer1 + altPlayer1 / 2
    and xDaBola + tamDaBola / 2 > xDoPlayer1 - altPlayer1 / 2):
        velDaBolaY = -velDaBolaY
    
    if (yDaBola - tamDaBola / 2 < yPlayer1 - largPlayer1 / 2
    and xDaBola - tamDaBola / 2 > xDoPlayer1 + altPlayer1 / 2
    and xDaBola + tamDaBola / 2 < xDoPlayer1 - altPlayer1 / 2):
        velDaBolaY = -velDaBolaY

    if yDaBola < -alt_jan / 2 or yDaBola > alt_jan / 2:
        xDaBola = 0
        yDaBola = 0

    if xDaBola < -larg_jan / 2 or xDaBola > larg_jan / 2:
        xDaBola = 0
        yDaBola = 0

    if yPlayer1 < -alt_jan / 2 or yPlayer1 > alt_jan / 2:
        yPlayer1 = 0

    if xDoPlayer1 < -larg_jan / 2 or xDoPlayer1 > larg_jan / 2:
        xDoPlayer1 = 0


    keys = pygame.key.get_pressed()

    if keys[K_UP]:
        yPlayer1 = yPlayer1 + 0.2
        altPlayer1 = 3 * tamDaBola
        largPlayer1 = tamDaBola

    if keys[K_DOWN]:
        yPlayer1 = yPlayer1 - 0.2
        altPlayer1 = 3 * tamDaBola
        largPlayer1 = tamDaBola

    if keys[K_RIGHT]:
        xDoPlayer1 = xDoPlayer1 + 0.2
        altPlayer1 = tamDaBola
        largPlayer1 = 3 * tamDaBola
    
    if keys[K_LEFT]:
        xDoPlayer1 = xDoPlayer1 - 0.2
        altPlayer1 = tamDaBola
        largPlayer1 = 3 * tamDaBola


def desenharRetangulo(x, y, larg, alt, r, g, b):
    glColor3f(r, g, b)

    glBegin(GL_QUADS)
    glVertex2f(-0.5 * larg + x, -0.5 * alt + y)
    glVertex2f(0.5 * larg + x, -0.5 * alt + y)
    glVertex2f(0.5 * larg + x, 0.5 * alt + y)
    glVertex2f(-0.5 * larg + x, 0.5 * alt + y)
    glEnd()


def desenhar():
    glViewport(0, 0, larg_jan, alt_jan)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-larg_jan / 2, larg_jan / 2, -alt_jan / 2, alt_jan / 2, 0, 1)

    glClear(GL_COLOR_BUFFER_BIT)

    desenharRetangulo(xDaBola, yDaBola, tamDaBola, tamDaBola, 1, 1, 0)
    desenharRetangulo(xDoPlayer1, yPlayer1, largPlayer1, altPlayer1, 1, 0, 0)

    pygame.display.flip()


pygame.init()
pygame.display.set_mode((larg_jan, alt_jan), DOUBLEBUF | OPENGL)

while True:
    atualizar()
    desenhar()
    pygame.event.pump()
