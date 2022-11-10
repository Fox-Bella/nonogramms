import pygame
from setup import *
from manager import Manager

pygame.init()
pygame.display.set_caption("Японские сканворды (РЕДАКТОР)")
size = [WIDTH, HEIGHT]
scene = pygame.display.set_mode(size)
clock = pygame.time.Clock()
playGame = True
deltatime = 0

# Рисует ли человек мышкой?
drawing = False

manager = Manager()

while playGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playGame = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                playGame = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False

    scene.fill((0, 0, 0))

    if (drawing):
        manager.click(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

    manager.draw(scene)

    pygame.display.flip()

    deltatime = clock.tick(FPS) / 1000