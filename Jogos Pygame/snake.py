import pygame
from pygame.locals import *
from sys import exit
from random import randrange

pygame.init()

larg = 640
alt = 480

tela = pygame.display.set_mode((larg, alt))
pygame.display.set_caption('Snake')
rel = pygame.time.Clock()

xApple = randrange(0, 620, 20)
yApple = randrange(0, 460, 20)

time = 0
tam = 20
tail = []
xSnake = 320
ySnake = 240
listSna = []
tamSnake = 1
right = left = up = down = False

def aumentaSnake(list, tamS, tamG):
    global tail

    for xy in range(len(list)-1, len(list)-(tamS+1), -1):
        pygame.draw.rect(tela, (0, 127, 0), (list[xy][0], list[xy][1], tamG, tamG))
        if xy != len(list)-1:
            tailXY = [list[xy][0], list[xy][1]]
            tail.append(tailXY)

def atualizar():
    global xSnake, ySnake, xApple, yApple, right, left, up, down, tamSnake, tam, listSna, tail, time

    apple = pygame.draw.rect(tela, (230, 0, 0), (xApple, yApple, tam, tam))
    snake = pygame.draw.rect(tela, (0, 127, 0), (xSnake, ySnake, tam, tam))

    if time % 5 == 0:

        if snake.colliderect(apple):
            xApple = randrange(0, 620, 20)
            yApple = randrange(0, 460, 20)
            tamSnake += 1
        
        if xSnake < 0 or xSnake >= larg or ySnake < 0 or ySnake >= alt:
            restart()
        for xy in tail:
            if snake.collidepoint(xy[0], xy[1]):
                restart()
                break
        tail = []

        listCab = []
        listCab.append(xSnake)
        listCab.append(ySnake)
        listSna.append(listCab)

        if right:
            xSnake += 20
        if left:
            xSnake -= 20
        if up:
            ySnake -= 20
        if down:
            ySnake += 20

    aumentaSnake(listSna, tamSnake, tam)
    
    keys = pygame.key.get_pressed()
    if keys[K_RIGHT] and left == False:
        right = True
        left = up = down = False
    if keys[K_LEFT] and right == False:
        left = True
        right = up = down = False
    if keys[K_UP] and down == False:
        up = True
        right = left = down = False
    if keys[K_DOWN] and up == False:
        down = True
        right = left = up = False

    time += 1


def restart():
    global xApple, yApple, tam, xSnake, ySnake, listSna, tamSnake, right, left, up, down, tail
    xApple = randrange(0, 620, 20)
    yApple = randrange(0, 460, 20)
    tam = 20
    tail = []
    xSnake = 320
    ySnake = 240
    listSna = []
    tamSnake = 1
    right = left = up = down = False


while True:
    tela.fill((0, 0, 0))

    rel.tick(50)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    atualizar()

    pygame.display.update()
