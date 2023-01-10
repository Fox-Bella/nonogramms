import pygame

import setup
from data.add_map import AddMap
from engine.buttons.buttons import Buttons
from engine.game import Game
from engine.screen.start_screen import StartScreen
from setup import *
from sound.sound import Sound

# Подсказки глючат
# Отключить кнопки при выигрыше

pygame.init()
pygame.display.set_caption("СКАН-МАТИК / Японские сканворды с математикой")
size = [WIDTH, HEIGHT]
scene = pygame.display.set_mode(size)
clock = pygame.time.Clock()
playGame = True
deltatime = 0

maps = AddMap()

buttons = Buttons()
sound = Sound(pygame)
game = Game(maps, sound)

mouse_button_pressed_1 = 0
mouse_button_pressed_3 = 0

start_screen = StartScreen()
if setup.error < 8:
    sound.play(Sound.START_PLAY_GAME)
else:
    start_screen.enabled = False

while playGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playGame = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                playGame = False
        # Если нет класса с выведенным примером для решения
        # и закончилась экранная заставка
        if setup.view_example is None:
            if event.type == pygame.MOUSEBUTTONDOWN and not start_screen.enabled:
                if mouse_button_pressed_1 == 0 and event.button == 1:
                    sound.play(Sound.CLICK)
                    game.press_mouse_1(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                    game.set_filling(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

                if mouse_button_pressed_3 == 0 and event.button == 3:
                    sound.play(Sound.CLICK)
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

    scene.fill("#1c3055")
    game.draw(scene, deltatime)

    if setup.view_example is not None:
        buttons.draw(scene, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], False)
        setup.view_example.draw(scene)
    elif not start_screen.enabled:
        pressed_btn = buttons.draw(scene, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], True)

        if pressed_btn == Buttons.AUTHORS:
            game.draw_authors(scene, deltatime)

        if pressed_btn == Buttons.PLAY:
            game.draw_play(scene, deltatime)

        if mouse_button_pressed_1 == 1 and pressed_btn != "NONE":
            mouse_button_pressed_1 = 0
            if pressed_btn == Buttons.CHECK:
                sound.play(Sound.CLICK)
                game.check_end_round()
            elif pressed_btn == Buttons.RESTART:
                sound.play(Sound.CLICK)
                game.start_level()
            elif pressed_btn == Buttons.HINT:
                sound.play(Sound.HELP)
                game.run_help()
            elif pressed_btn == Buttons.MATH_30:
                sound.play(Sound.COMPLEXITY)
                setup.difficulty = 1
                game.start_level()
            elif pressed_btn == Buttons.MATH_60:
                sound.play(Sound.COMPLEXITY)
                setup.difficulty = 2
                game.start_level()
            elif pressed_btn == Buttons.MATH_100:
                sound.play(Sound.COMPLEXITY)
                setup.difficulty = 0
                game.start_level()
            elif pressed_btn == Buttons.NEXT:
                sound.play(Sound.CLICK)
                setup.level += 1
                if setup.level == len(game.maps.level) or setup.level == setup.max_level + 1:
                    setup.level -= 1
                game.start_level()
            elif pressed_btn == Buttons.PREV:
                sound.play(Sound.CLICK)
                setup.level -= 1
                if setup.level < 0:
                    setup.level = 0
                else:
                    game.start_level()
            elif pressed_btn == Buttons.EXIT:
                setup.save()
                playGame = False
            elif pressed_btn == Buttons.RESET_GAME:
                sound.play(Sound.CLICK)
                setup.reset()
                game.gamestate = Game.PLAY_GAME
                game.start_level()

    if start_screen.alpha > 0:
        start_screen.draw(scene, deltatime)

    pygame.display.flip()

    # Если не отображено окно с примером, то работаем с мышкой и основным полем
    if setup.view_example is None:
        if mouse_button_pressed_1 == 1:
            game.mouse_1_button_down(mouse_button_pressed_1, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        if mouse_button_pressed_3 == 3:
            game.mouse_3_button_down(mouse_button_pressed_3, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

    game.act(deltatime, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

    deltatime = clock.tick(FPS) / 1000

pygame.quit()
setup.save()