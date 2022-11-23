import setup
from setup import *
from data.add_map import AddMap
from engine.game import Game
import pygame

# Добавить чтобы работал pygame
pygame.init()
pygame.display.set_caption("Матемонские японворды // Математика + Японский сканворд")
size = [WIDTH, HEIGHT]
scene = pygame.display.set_mode(size)
clock = pygame.time.Clock()
playGame = True
deltatime = 0

maps = AddMap()
game = Game(maps)

mouse_button_pressed_1 = 0

while playGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playGame = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                playGame = False
        # Если нет класса с выведенным примером для решения
        if setup.view_example is None:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_button_pressed_1 == 0:
                    game.press_mouse_1(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                    game.set_filling(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                mouse_button_pressed_1 = event.button
                if mouse_button_pressed_1 == 3:
                    game.mouse_3_button_down(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_button_pressed_1 = 0
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    setup.view_example.press_mouse_button_1(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

    scene.fill((0, 0, 0))
    game.draw(scene, deltatime)

    if not (setup.view_example is None):
        setup.view_example.draw(scene)

    pygame.display.flip()

    if setup.view_example is None:
        if mouse_button_pressed_1 == 1 or mouse_button_pressed_1 == 3:
            game.mouse_button_down(mouse_button_pressed_1, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        game.act(deltatime, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

    deltatime = clock.tick(FPS) / 1000
