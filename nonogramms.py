from data.add_map import AddMap
from setup import *
import pygame

# Добавить чтобы работал pygame
pygame.init()
pygame.display.set_caption("Японские сканворды (РЕДАКТОР)")
size = [WIDTH, HEIGHT]
scene = pygame.display.set_mode(size)
clock = pygame.time.Clock()
playGame = True
deltatime = 0

level = AddMap()

while playGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playGame = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                playGame = False

    scene.fill((0, 0, 0))

    pygame.display.flip()

    deltatime = clock.tick(FPS) / 1000