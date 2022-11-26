import pygame

import setup
from setup import *
from engine.screen.view_example import ViewExample
from random import randint

"""
    Содержимое ячейки с цифрой.
    Здесь же выводится пример для решения.
"""
class Cell:

    def __init__(self, value, x, y, size_field, font, text_color):
        self.value = value
        self.font = font
        self.text_color = text_color
        self.x = x
        self.y = y
        self.size_field = size_field

        # Неправильное значение?
        # self.error_digit = True
        # self.print_to_screen = "?"

        self.error_digit = False
        self.print_to_screen = f"{value}"

        # self.print_to_screen = f"{value}"
        self.bg = False

    def set_error_digit(self):
        self.error_digit = True
        self.print_to_screen = "?"

    def draw(self, scene: pygame.surface):
        key = f"cell_{self.x}{self.y}"

        if self.print_to_screen == "?":
            pygame.draw.rect(scene, TEXT_LIGHT_ATTENTION,
                             (self.x + (self.size_field - self.size_field // 2) // 2 , self.y,
                              self.size_field // 2, 21))
            # srf = self.font.getSystemText(key, f"{self.value}", color=TEXT_COLOR)
            srf = self.font.getSystemText(key, f"{self.print_to_screen}", COLOR_DEEP_GRAY)
            corrX = (self.size_field - srf.get_width()) // 2
        else:
            # srf = self.font.getSystemText(key, f"{self.value}", color=TEXT_COLOR)
            srf = self.font.getSystemText(key, f"{self.print_to_screen}", self.text_color)
            corrX = (self.size_field - srf.get_width()) // 2

        if self.bg:
            if self.error_digit:
                pygame.draw.rect(scene, TEXT_LIGHT_BAD, (self.x, self.y, self.size_field, 21))
            else:
                pygame.draw.rect(scene, TEXT_LIGHT_GOOD, (self.x, self.y, self.size_field, 21))
        scene.blit(srf, (self.x + corrX, self.y))

    def check_mouse(self, x, y):
        if self.x < x < self.x + self.size_field and \
           self.y < y < self.y + 31:
            self.bg = True
            return True
        else:
            self.bg = False
        return False

    def press_mouse_1(self, x, y):
        if self.print_to_screen != "?" and self.error_digit == False:
            return False
        if self.bg:
            if setup.view_example is None:
                setup.view_example = ViewExample(self.x, self.y, self.size_field, self.value, self)

    def delete_view_example(self):
        setup.view_example = None


