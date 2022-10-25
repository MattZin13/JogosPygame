import pygame
from pygame.locals import *
from sys import exit

pygame.init()

larg = 640
alt = 480

tela = pygame.display.set_mode((larg, alt))
pygame.display.set_caption('-Deflect-')
rel = pygame.time.Clock()

def atualizar():
  global larg

  keys = pygame.key.get_pressed()

while True:
  tela.fill((0, 0, 0))

  rel.tick(100)
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      exit()

    atualizar()

    pygame.display.update()
