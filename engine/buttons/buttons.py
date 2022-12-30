import pygame
from engine.buttons.button import Button
from engine.font import Font
import setup


class Buttons:

    PLAY = 0
    CHECK = 1
    RESTART = 2
    HINT = 3
    MATH_30 = 4
    MATH_60 = 5
    MATH_100 = 6
    NEXT = 7
    PREV = 8
    EXIT = 9
    RESET_GAME = 10
    AUTHORS = 11

    def __init__(self):
        self.buttons = []
        font = Font()
        self.buttons.append(Button(Buttons.PLAY, 795, 540, ["button_question.png", "button_question_act.png"], "Как играть", font))
        self.buttons.append(Button(Buttons.CHECK, 795, 220, ["button_check_deact.png", "button_check_act.png"], "Правильно ли решено? Если нет, то увеличатся ошибки", font))
        self.buttons.append(Button(Buttons.RESTART, 795, 280, ["button_restart_deact.png", "button_restart_act.png"], "Начать раунд заново", font))
        self.buttons.append(Button(Buttons.HINT, 795, 340, ["button_hint_deact.png", "button_hint_act.png"], "Подсказать 1-3 случайные клетки", font))

        self.buttons.append(Button(Buttons.NEXT, 795, 400, ["button_next_deact.png", "button_next_act.png"], "Следующая головоломка", font))
        self.buttons.append(Button(Buttons.PREV, 795, 430, ["button_prev_deact.png", "button_prev_act.png"], "Предыдущая головоломка", font))
        self.buttons.append(Button(Buttons.EXIT, 795, 470, ["button_exit_deact.png", "button_exit_act.png"], "Выход из игры", font))
        self.buttons.append(Button(Buttons.RESET_GAME, 795, 500, ["button_reset_deact.png", "button_reset_act.png"], "Сбросить всё и вернуться к началу игры", font))

        self.buttons_difficulty = []
        self.buttons_difficulty.append(Button(Buttons.MATH_30, 795, 310, ["button_math30_deact.png", "button_math30_act.png"], "Треть чисел скрыта выражениями", font))
        self.buttons_difficulty.append(Button(Buttons.MATH_60, 795, 310, ["button_math60_deact.png", "button_math60_act.png"], "Скрыто выражениями чуть больше половины чисел", font))
        self.buttons_difficulty.append(Button(Buttons.MATH_100, 795, 310, ["button_math100_deact.png", "button_math100_act.png"], "Все числа представлены выражениями", font))

        self.buttons.append(Button(Buttons.AUTHORS, 795, setup.HEIGHT - 40, ["button_authors_deact.png", "button_authors_act.png"], "Те, кто старался", font))

    def draw(self, scene, mouse_x, mouse_y, pressable):
        return_id_button = "NONE"
        res = "NONE"
        for btn in self.buttons:
            if btn.id_button == Buttons.HINT and setup.hint > 0 and setup.error < 8:
                res = btn.draw(scene, mouse_x, mouse_y, pressable)
            elif btn.id_button == Buttons.NEXT and setup.level < setup.max_level and setup.error < 8:
                res = btn.draw(scene, mouse_x, mouse_y, pressable)
            elif btn.id_button == Buttons.PREV and setup.level > 0 and setup.error < 8:
                res = btn.draw(scene, mouse_x, mouse_y, pressable)
            elif btn.id_button != Buttons.HINT and \
                 btn.id_button != Buttons.NEXT and \
                 btn.id_button != Buttons.PREV and setup.error < 8:
                res = btn.draw(scene, mouse_x, mouse_y, pressable)
            elif setup.error >= 8 and (btn.id_button == Buttons.EXIT or btn.id_button == Buttons.RESET_GAME):
                res = btn.draw(scene, mouse_x, mouse_y, pressable)

            if res != "NONE":
                return_id_button = res

        if setup.error < 8:
            res = self.buttons_difficulty[setup.difficulty].draw(scene, mouse_x, mouse_y, pressable)

        if res != "NONE":
            return_id_button = res

        return return_id_button

