import pygame
from pygame.locals import *
from sys import exit
from random import randint
from time import sleep

pygame.init()

larg = 640
alt = 480

tela = pygame.display.set_mode((larg, alt))
pygame.display.set_caption('Space')

fonteP = pygame.font.SysFont('microsoftyahei', 25, False, False)
fontBase = pygame.font.SysFont('microsofthimalaya', 40, False, False)
fontFinal = pygame.font.SysFont('gabriola', 40, False, False)
pontFinal = pygame.font.SysFont('georgia', 40, True, False)
pont = pygame.font.SysFont('microsoftyahei', 25, False, False)

rel = pygame.time.Clock()

tamPlayer = 28
xPlayer = tamPlayer / 2
yPlayer = alt / 2
vidaP = 3
vidaBase = 10

altLasers = 5
xLaser = xLaserE = xRed = xBlue = xLaserB = xShield = larg
yLaser = yLaserE = yRed = yBlue = yLaserB = yShield = alt
velLaser = velRed = time = extime = velLaserE = timeR = extimeR = velBlue = extimeEsp = timeEsp = pontos = timeEsp = coldown = 0
laseAct = redAct = laseEAct = blueAct = final = shieldAct = espAct = False

raioEsp = 7.5
xEsp = 0 - raioEsp
yEsp = 0 - raioEsp

tamRed = 35
vidaR = 2
tamBlue = 20


def atualizar():
    global yPlayer, xLaser, yLaser, laseAct, velLaser, xRed, yRed, time, extime, redAct, velRed, vidaP, xLaserE, yLaserE
    global velLaserE, laseEAct, timeR, extimeR, vidaR, vidaBase, xBlue, yBlue, blueAct, velBlue, pontos, final, extimeEsp
    global xEsp, yEsp, shieldAct, espAct, xShield, yShield, timeEsp, coldown

    player = pygame.draw.rect(tela, (255, 255, 255), (xPlayer, yPlayer, tamPlayer, tamPlayer))
    laser = pygame.draw.rect(tela, (255, 100, 0), (xLaser, yLaser, tamPlayer, altLasers))
    red = pygame.draw.rect(tela, (255, 0, 0), (xRed, yRed, tamRed, tamRed))
    laserE = pygame.draw.rect(tela, (160, 100, 0), (xLaserE, yLaserE, tamPlayer, altLasers))
    blue = pygame.draw.rect(tela, (0, 0, 255), (xBlue, yBlue, tamBlue, tamBlue))
    especial = pygame.draw.circle(tela, (0, 150, 255), (xEsp, yEsp), raioEsp)
    shield = pygame.draw.rect(tela, (255, 150, 0), (xShield, yShield, altLasers, tamPlayer))

    if final:
        tela.fill((0, 30, 0))
        tela.blit(formatedFinal, (tamRed * 2, tamRed))
        tela.blit(formatedFinal2, (tamRed * 2, tamRed + 40))
        tela.blit(formatedFinal3, (tamRed * 2, tamRed + 80))
        tela.blit(formatedFinal4, (tamRed * 2, tamRed + 120))
        pygame.display.update()
        sleep(2)
        tela.blit(pormatedFinal, (tamRed * 2, alt - tamRed - 40))
        pygame.display.update()
        sleep(8)
        final = False
        tela.fill((0, 0, 0))
        pontos = 0

    if laseAct:
        velLaser = 3
        xLaser += velLaser
        if xLaser > larg or laser.colliderect(red) or laser.colliderect(blue):
            xLaser = larg
            yLaser = alt
            laseAct = False
            velLaser = 0
            coldown = time
            if laser.colliderect(blue):
                pontos += 1

    if redAct:
        velRed = 0.5
        xRed -= velRed
        timeR += 1
        if red.colliderect(player) or red.colliderect(laser):
            vidaR -= 1
            if red.colliderect(player):
                vidaP -= 1
        if xRed + tamRed < 0 or vidaR == 0 or red.colliderect(shield):
            if xRed + tamRed < 0:
                vidaBase -= 1
            velRed = timeR = extimeR = 0
            xRed = larg
            yRed = alt
            redAct = False
            vidaR = 3
            pontos += 3
        if timeR - extimeR == 150 and not (laseEAct):
            laseEAct = True
            xLaserE = xRed - tamRed
            yLaserE = yRed + tamRed / 2
            extimeR = timeR
        if laseEAct:
            extimeR = timeR

    if laseEAct:
        velLaserE = 3
        xLaserE -= velLaserE
        if laserE.colliderect(player):
            xLaserE = larg
            yLaserE = alt
            laseEAct = False
        if xLaserE + tamPlayer < 0 or laserE.colliderect(player) or laserE.colliderect(shield):
            xLaserE = larg
            yLaserE = alt
            laseEAct = False
            if laserE.colliderect(player):
                vidaP -= 1
            elif laserE.colliderect(laser):
                coldown = time
            else:
                vidaBase -= 1
        if laserE.colliderect(laser):
            xLaser = xLaserE = larg
            yLaser = yLaserE = alt
            laseAct = laseEAct = False

    if blueAct:
        velBlue = 3
        xBlue -= velBlue
        if xBlue + tamBlue < 0 or blue.colliderect(laser) or blue.colliderect(shield):
            if xBlue + tamBlue < 0:
                vidaBase -= 1
            velBlue = 0
            xBlue = larg
            yBlue = alt
            blueAct = False
            if blue.colliderect(player):
                vidaP -= 1

    if espAct:
        xEsp -= 1
        if especial.colliderect(player) or xEsp + raioEsp < 0:
            espAct = False
            xEsp = 0 - raioEsp
            yEsp = 0 - raioEsp
            if especial.colliderect(player):
                shieldAct = True
                timeEsp = time

    if shieldAct:
        xShield = xPlayer + tamPlayer + 7
        yShield = yPlayer
        if time - timeEsp == 1000:
            xShield = larg
            yShield = alt
            shieldAct = False

    keys = pygame.key.get_pressed()

    if keys[K_UP] and yPlayer > 0:
        yPlayer -= 2
    if keys[K_DOWN] and yPlayer + tamPlayer < alt:
        yPlayer += 2
    if keys[K_SPACE] and not(laseAct) and time - coldown >= 25:
        laseAct = True
        xLaser = xPlayer + tamPlayer
        yLaser = yPlayer + tamPlayer / 2
        coldown = time

    if time - extime == 700:
        extime = time
        if not(redAct):
            yRed = randint(0, alt - tamRed)
            xRed = larg - tamRed
            redAct = True
            extime += 200
        if not(blueAct):
            yBlue = randint(0, alt - tamBlue)
            xBlue = larg - tamBlue
            blueAct = True
            extime += 200

    if time - extimeEsp == 0:
        timeEsp = randint(2500, 3500)
        print(timeEsp)
    elif time - extimeEsp == timeEsp:
        espAct = True
        xEsp = larg
        yEsp = randint(0 + 4, alt - 4)
        extimeEsp = time

    time += 1


def restart():
    global xPlayer, yPlayer, vidaP, vidaR, vidaBase, xLaser, xLaserE, xRed, yLaser, yLaserE, yRed, velLaser, velRed, time
    global extime, velLaserE, timeR, extimeR, laseAct, redAct, laseEAct, shieldAct, espAct, xShield, yShield, xEsp, yEsp

    xPlayer = tamPlayer / 2
    yPlayer = alt / 2
    vidaP = vidaR = 3
    vidaBase = 10
    xLaser = xLaserE = xRed = xShield = larg
    yLaser = yLaserE = yRed = yShield = alt
    velLaser = velRed = time = extime = velLaserE = timeR = extimeR = 0
    xEsp = yEsp = 0 - raioEsp
    laseAct = redAct = laseEAct = shieldAct = espAct = False


while True:
    tela.fill((0, 0, 0))

    formatedP = fonteP.render(f'Vida: {vidaP}', False, (255, 255, 255))
    formatedBase = fontBase.render(f'Base: {vidaBase}', False, (127, 127, 127))
    formatedFinal = fontFinal.render(f'Parabéns, você venceu!', False, (255, 255, 255))
    formatedFinal2 = fontFinal.render(f'Você ficou com: {vidaP} pontos e vida', False, (255, 255, 255))
    formatedFinal3 = fontFinal.render(f'Base com: {vidaBase} de resistência', False, (255, 255, 255))
    formatedFinal4 = fontFinal.render(f'Com {pontos} pontos', False, (255, 255, 255))
    pormatedFinal = pontFinal.render(f'Pontuação final: {vidaBase * 2 + vidaP + pontos}', False, (127, 254, 0))
    pormated = pont.render(f'Pontos: {pontos}', False, (255, 255, 255))

    if vidaP == 0 or vidaBase == 0:
        restart()
        pontos = 0
        final = True

    rel.tick(100)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    atualizar()

    tela.blit(pormated, (tamPlayer / 2, alt - tamPlayer * 4))
    tela.blit(formatedP, (tamPlayer / 2, alt - tamPlayer * 2))
    tela.blit(formatedBase, (tamPlayer / 2, 0 + tamPlayer * 2))
    pygame.display.update()
