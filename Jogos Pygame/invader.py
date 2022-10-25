import pygame
from pygame.locals import *
from sys import exit
from random import randint
from time import sleep

pygame.init()

pygame.mixer.music.set_volume(0.1)
fundo = pygame.mixer.music.load('Visager - Battle!.mp3')
pygame.mixer.music.play(-1)

win = pygame.mixer.Sound('smw_castle_clear.wav')
lose = pygame.mixer.Sound('smw_lost_a_life.wav')
laser = pygame.mixer.Sound('344276__nsstudios__laser3.wav')
EnemyDam = pygame.mixer.Sound('361636__jofae__8-bit-slam.mp3')
PlayerDam = pygame.mixer.Sound('350921__cabled-mess__hurt-c-03.wav')
lasersImpact = pygame.mixer.Sound('170148__timgormly__8-bit-hurt1.aiff')

larg = 640
alt = 480

def posZX(tam):
    return larg / 2 - tam

tela = pygame.display.set_mode((larg, alt))
pygame.display.set_caption(('The Invader'))

fontP = pygame.font.SysFont('sans', 20, False, True)
fontE = pygame.font.SysFont('georgia', 20, True, False)

tamPlayer = 20
xPlayer = posZX(tamPlayer)
yPlayer = alt - ( tamPlayer + tamPlayer / 2)
vidaPt = 3

tamEnemy = tamPlayer * 3
xEnemy = posZX(tamEnemy)
yEnemy = tamPlayer / 2
velEnemyX = 1.4
Y = 3
vidaEt1 = 6
vidaEt2 = 9
vidaEt3 = 12

largTP = raioTE = 5
altTP = tamPlayer
xTP = larg
yTP = alt

xTE1 = yTE1 = xTE2 = yTE2 = xTE3 = yTE3 = 0 - raioTE / 2

time = extime = velTP = velTE1 = velXTE2 = velYTE2 = velYTE3 = velXTE3 = vidaP = vidaE = level = 0
tiroP = tiroE1 = tiroE2 = tiroE3 = False
change = randint(1, 2)

tabP = ((255, 255, 255), (208, 208, 208), (161, 161, 161))
tabE = (((255, 165, 0), (242, 152, 0), (229, 139, 0), (216, 126, 0), (203, 113, 0), (190, 100, 0)), 
((202, 36, 100), (198, 32, 96), (194, 27, 92), (190, 23, 88), (186, 18, 84), 
(182, 14, 80), (182, 13, 80), (178, 9, 76), (174, 0, 72)),
((103, 33, 205), (100, 30, 202), (97, 27, 199), (94, 24, 196), (91, 21, 193), (88, 18, 190), 
(85, 15, 187), (82, 12, 184), (79, 9, 181), (76, 6, 178), (73, 3, 175), (70, 0, 172)))

rel = pygame.time.Clock()


def atualizar():
    global xPlayer, yPlayer, xEnemy, yEnemy, velEnemyX, time, extime, yTP, yTE1, velTP, velTE1, xTP, xTE1, vidaP, vidaE, tiroP, tiroE1, level, velXTE2, velYTE2, velXTE3, velYTE3, xTE2, yTE2, xTE3, yTE3, tiroE2, tiroE3, Y, vidaPt, vidaEt1, vidaEt2, vidaEt3

    corP = tabP[vidaP][:]
    corE = tabE[level][vidaE][:]

    if level == 1:
        if velEnemyX > 0:
            velEnemyX = 2.4
        if velEnemyX < 0:
            velEnemyX = -2.4
        Y = 6
    if level == 2:
        if velEnemyX > 0:
            velEnemyX = 4
        if velEnemyX < 0:
            velEnemyX = -4
        Y = 9

    if change == 1:
        xEnemy += velEnemyX
    elif change == 2:
        xEnemy -= velEnemyX

    player = pygame.draw.rect(tela, (corP[0], corP[1], corP[2]), (xPlayer, yPlayer, tamPlayer, tamPlayer))
    enemy = pygame.draw.rect(tela, (corE[0], corE[1], corE[2]), (xEnemy, yEnemy, tamEnemy, tamEnemy))
    tp = pygame.draw.rect(tela, (0, 255, 0), (xTP, yTP, largTP, altTP))
    te1 = pygame.draw.circle(tela, (255, 0, 0), (xTE1, yTE1), raioTE)
    te2 = pygame.draw.circle(tela, (153, 0, 153), (xTE2, yTE2), raioTE)
    te3 = pygame.draw.circle(tela, (153, 0, 153), (xTE3, yTE3), raioTE)

    if xEnemy < 0 or xEnemy + tamEnemy > larg:
        velEnemyX = -velEnemyX
        yEnemy += Y
      
    if tiroP:
        velTP = 3.5
        yTP -= velTP
        if tp.colliderect(te1):
            velTP = velTE1 = 0
            xTP = larg
            yTP = alt
            xTE1 = yTE1 = 0 - raioTE / 2
            tiroP = False
            lasersImpact.play()
        if tp.colliderect(te2):
            velTP = velXTE2 = velYTE2 = 0
            xTP = larg
            yTP = alt
            xTE2 = yTE2 = 0 - raioTE / 2
            tiroP = False
            lasersImpact.play()
        if tp.colliderect(te3):
            velTP = velXTE3 = velYTE3 = 0
            xTP = larg
            yTP = alt
            xTE3 = yTE3 = 0 - raioTE / 2
            tiroP = False
            lasersImpact.play()
        if tp.colliderect(enemy):
            if level == 0:
                vidaEt1 -= 1
            if level == 1:
                vidaEt2 -= 1
            if level == 2:
                vidaEt3 -= 1
            vidaE += 1
            xTP = larg
            yTP = alt
            velTP = 0
            tiroP = False
            EnemyDam.play()
            
    if tiroE1:
        yTE1 += velTE1
        if te1.colliderect(player):
            vidaP += 1
            vidaPt -= 1
            xTE1 = yTE1 = 0 - raioTE / 2
            velTE1 = 0
            tiroE1 = False
            PlayerDam.play()

    if tiroE2:
        yTE2 += velYTE2
        xTE2 += velXTE2
        if te2.colliderect(player):
            vidaP += 1
            vidaPt -= 1
            xTE2 = yTE2 = 0 - raioTE / 2
            velXTE2 = velYTE2 = 0
            tiroE2 = False
            PlayerDam.play()

    if tiroE3:
        yTE3 += velYTE3
        xTE3 += velXTE3
        if te3.colliderect(player):
            vidaP += 1
            vidaPt -= 1
            xTE3 = yTE3 = 0 - raioTE / 2
            velXTE3 = velYTE3 = 0
            tiroE3 = False
            PlayerDam.play()
    
    if yTP < 0:
        velTP = 0
        xTP = larg
        yTP = alt
        tiroP = False

    if yTE1 + raioTE / 2 > alt:
        velTE1 = -velTE1

    if yTE1 - raioTE / 2 < 0:
        velTE1 = 0
        tiroE1 = False
        xTE1 = yTE1 = 0 - raioTE / 2

    if yTE2 + raioTE / 2 > alt:
        velYTE2 = -velYTE2

    if yTE2 - raioTE / 2 < 0:
        velYTE2 = velXTE2 = 0
        tiroE2 = False
        xTE2 = yTE2 = 0 - raioTE / 2

    if xTE2 - raioTE / 2 < 0 or xTE2 + raioTE / 2 > larg:
        velXTE2 = -velXTE2

    if yTE3 + raioTE / 2 > alt:
        velYTE3 = -velYTE3

    if yTE3 - raioTE / 2 < 0:
        velYTE3 = velXTE3 = 0
        tiroE3 = False
        xTE3 = yTE3 = 0 - raioTE / 2

    if xTE3 - raioTE / 2 < 0 or xTE3 + raioTE / 2 > larg:
        velXTE3 = -velXTE3

    keys = pygame.key.get_pressed()

    if xPlayer > 0:
        if keys[K_LEFT]:
            xPlayer -= 1.3
    if xPlayer < larg:
        if keys[K_RIGHT]:
            xPlayer +=  1.3
    if tiroP == False:
        if keys[K_SPACE]:
            tiroP = True
            xTP = xPlayer
            yTP = yPlayer
            laser.play()

    if level == 0:
        if vidaE == 6:
            vidaE = velTP = velTE1 = 0
            tiroP = tiroE1 = False
            xPlayer = posZX(tamPlayer)
            yPlayer = alt - ( tamPlayer + tamPlayer / 2)
            xEnemy = posZX(tamEnemy)
            yEnemy = tamPlayer / 2
            xTP = larg
            yTP = alt
            xTE1 = yTE1 = 0 - raioTE / 2
            level += 1
            coldown = True
    if level == 1:
        if vidaE == 9:
            vidaE = velTP = velTE1 = 0
            tiroP = tiroE1 = False
            xPlayer = posZX(tamPlayer)
            yPlayer = alt - ( tamPlayer + tamPlayer / 2)
            xEnemy = posZX(tamEnemy)
            yEnemy = tamPlayer / 2
            xTP = larg
            yTP = alt
            xTE1 = yTE1 = 0 - raioTE / 2
            level += 1
            coldown = True
    if level == 2:
        if vidaE == 12:
            vidaE = velTP = velTE1 = 0
            tiroP = tiroE1 = False
            xPlayer = posZX(tamPlayer)
            yPlayer = alt - ( tamPlayer + tamPlayer / 2)
            xEnemy = posZX(tamEnemy)
            yEnemy = tamPlayer / 2
            xTP = larg
            yTP = alt
            xTE1 = yTE1 = 0 - raioTE / 2
            level += 1
        
    if vidaP == 3 or level == 3 or enemy.colliderect(player):
        vidaE = vidaP = velTP = velTE1 = 0
        tiroP = tiroE1 = False
        xPlayer = posZX(tamPlayer)
        yPlayer = alt - ( tamPlayer + tamPlayer / 2)
        xEnemy = posZX(tamEnemy)
        yEnemy = tamPlayer / 2
        xTP = larg
        yTP = alt
        xTE1 = yTE1 = 0 - raioTE / 2
        velEnemyX = 1.4
        Y = 3
        vidaPt = 3
        vidaEt1 = 6
        vidaEt2 = 9
        vidaEt3 = 12
        if level == 3:
            win.play()
            sleep(9)
        else:
            lose.play()
            sleep(4)
        pygame.mixer.music.play(-1)
        level = 0

    if time - extime == 600:
        if level == 0:
            tiroE1 = True
            velTE1 = 2
            xTE1 = xEnemy + tamEnemy / 2
            yTE1 = yEnemy + tamEnemy
        if level == 1:
            tiroE2 = tiroE3 = True
            velXTE2 = velYTE2 = velYTE3 = 2
            velXTE3 = -2
            xTE2 = xTE3 = xEnemy + tamEnemy / 2
            yTE2 = yTE3 = yEnemy + tamEnemy
        if level == 2:
            tiroE2 = tiroE3 = tiroE1 = True
            velXTE2 = velYTE2 = velYTE3 = velTE1 = 2
            velXTE3 = -2
            xTE2 = xTE3 = xTE1 = xEnemy + tamEnemy / 2
            yTE2 = yTE3 = yTE1 = yEnemy + tamEnemy
        extime = time

    time += 1


while True:
    tela.fill((0, 0, 0))

    rel.tick(100)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    textP = f'Player: {vidaPt}'
    formatedP = fontP.render(textP, False, (255, 255, 255))
    if level == 0:
        textE = f'Invader: {vidaEt1}'
    elif level == 1:
        textE = f'Invader 2.0: {vidaEt2}'
    else:
        textE = f'Invader 3.0: {vidaEt3}'
    formatedE = fontE.render(textE, False, (tabE[level][0]))
    
    atualizar()

    tela.blit(formatedP, (190, 440))
    tela.blit(formatedE, (450, 40))
    pygame.display.update()
