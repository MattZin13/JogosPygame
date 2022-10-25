import pygame
from pygame.locals import *
from sys import exit

pygame.init()

larg = 800
alt = 640

tela = pygame.display.set_mode((larg, alt))
pygame.display.set_caption('Simulação de Gravidade')
rel = pygame.time.Clock()

posXa = larg / 2
posYa = alt / 2 - 80
posXb = larg / 2
posYb = alt / 2 + 80
posXc = larg / 2
posYc = alt / 2
velXa = 0.1
velYa = 0
vela = ((velXa)**2 + (velYa)**2)**(1/2)
velXb = 0
velYb = 0
velb = ((velXb)**2 + (velYb)**2)**(1/2)
velXc = 0
velYc = 0
acelXa = 0
acelYa = 0
acelXb = 0
acelYb = 0
acelXc = 0
acelYc = 0
m1 = 10
m2 = 10
m3 = 10
ra = 15
rb = 15
rc = 15
stop = False


def atualizar():
    global posXa, posYa, velXa, velYa, acelXa, acelYa, acelXb, acelYb, velXb, velYb, posXb, posYb, F, d, stop

    d = ((posXa - posXb)**2 + (posYa - posYb)**2)**(1/2)
    F = (m1 * m2 / d**2)

    if d > (ra + rb):
        acelXa = F / m1 * (posXb - posXa) / d
        acelYa = F / m1 * (posYa - posYb) / d
        acelXb = F / m2 * (posXa - posXb) / d
        acelYb = F / m2 * (posYb - posYa) / d
        velXa += acelXa
        velYa += acelYa
        velXb += acelXb
        velYb += acelYb
        posXa += velXa
        posYa -= velYa
        posXb += velXb
        posYb -= velYb
    else:
        stop = True

    pygame.draw.circle(tela, (255, 0, 0), (posXa, posYa), ra)
    pygame.draw.circle(tela, (0, 0, 255), (posXb, posYb), rb)
    pygame.draw.circle(tela, (0, 255, 0), (posXc, posYc), rc)


while True:
    tela.fill((0, 0, 0))

    if stop:
        break

    rel.tick(150)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    atualizar()

    pygame.display.update()
