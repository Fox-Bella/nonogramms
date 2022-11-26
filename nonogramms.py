import setup
from setup import *
# from data.add_map import AddMap
from data.add_map23456790 import AddMap
from engine.game import Game
from engine.buttons.buttons import Buttons
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
buttons = Buttons()

mouse_button_pressed_1 = 0
mouse_button_pressed_3 = 0

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
                if mouse_button_pressed_1 == 0 and event.button == 1:
                    game.press_mouse_1(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                    game.set_filling(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

                if mouse_button_pressed_3 == 0 and event.button == 3:
                    game.set_blocked(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

                mouse_button_pressed_1 = event.button
                mouse_button_pressed_3 = event.button

            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_button_pressed_1 = 0
                mouse_button_pressed_3 = 0
        else:
            mouse_button_pressed_1 = 0
            mouse_button_pressed_3 = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    setup.view_example.press_mouse_button_1(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

    scene.fill((0, 0, 0))
    game.draw(scene, deltatime)

    if not (setup.view_example is None):
        buttons.draw(scene, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], False)
        setup.view_example.draw(scene)
    else:
        pressed_btn = buttons.draw(scene, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], True)
        if mouse_button_pressed_1 == 1 and pressed_btn != "NONE":
            mouse_button_pressed_1 = 0
            if pressed_btn == Buttons.CHECK:
                print("Проверка")
            elif pressed_btn == Buttons.RESTART:
                pass
            elif pressed_btn == Buttons.HINT:
                pass
            elif pressed_btn == Buttons.MATH_30:
                setup.difficulty = 1
                game.start_level()
            elif pressed_btn == Buttons.MATH_60:
                setup.difficulty = 2
                game.start_level()
            elif pressed_btn == Buttons.MATH_100:
                setup.difficulty = 0
                game.start_level()
            elif pressed_btn == Buttons.NEXT:
                pass
            elif pressed_btn == Buttons.PREV:
                pass
            elif pressed_btn == Buttons.EXIT:
                pass
            elif pressed_btn == Buttons.RESET_GAME:
                pass

    pygame.display.flip()

    # Если не отображено окно с примером, то работаем с мышкой и основным полем
    if setup.view_example is None:
        if mouse_button_pressed_1 == 1:
            game.mouse_1_button_down(mouse_button_pressed_1, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        if mouse_button_pressed_3 == 3:
            game.mouse_3_button_down(mouse_button_pressed_3, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

    game.act(deltatime, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

    deltatime = clock.tick(FPS) / 1000
