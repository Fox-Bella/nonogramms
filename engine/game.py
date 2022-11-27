import random

import pygame

import setup
from setup import *
from engine.square import Square
from engine.horizontal import Horizontal
from engine.vertical import Vertical
from engine.errors.errors import Error
from engine.font import Font
from engine.screen.label_text import LabelText
from engine.errors.helper import Helper


class Game:

    def __init__(self, maps):
        self.maps = maps
        self.current_map = None
        self.fields = None
        self.i_line_cells = None
        self.j_line_cells = None
        self.size_field = None
        self.start_x = None
        self.start_y = None
        self.i_count_fields = None
        self.j_count_fields = None
        self.end_x = None
        self.end_y = None
        self.horizontal = None
        self.vertical = None
        self.fill = True
        self.blocked = True
        self.width = None
        self.height = None

        # Шрифт
        self.font = Font()

        # Вывод текстовых меток
        self.label_text = LabelText(self.font)

        # Считаем кадры, чтобы разгрузить процессор на проверках
        self.frame = 0

        # Чтобы не срабатывала ошибка дважды на одну и ту же клетку
        self.last_i = -1
        self.last_j = -1

        # Здесь анимация ошибок
        self.errors = []

        # Здесь анимация подсказок
        self.helper = []

        self.start_level()

    def start_level(self):

        # Текущая карта
        self.current_map = self.maps.level[level].data_level

        # Текущая карта с True или False
        # Самое коряво написанное, но быстрое копирование в Python
        self.fields = [f[:] for f in self.current_map]

        self.size_field = square_game_sizes[max(len(self.fields), len(self.fields[0])) - 1]

        self.i_count_fields = len(self.current_map)
        self.j_count_fields = len(self.current_map[0])

        self.width = self.j_count_fields * self.size_field
        self.height = self.i_count_fields * self.size_field

        self.start_x = (795 - self.width) // 2
        self.start_y = (HEIGHT - self.height) // 2 + 100

        self.horizontal = Horizontal(self.current_map, self.start_x, self.start_y, self.size_field, self.font)
        self.vertical = Vertical(self.current_map, self.start_x, self.start_y, self.size_field, self.font)

        self.start_x = (795 - self.width + self.vertical.width) // 2
        self.start_y = (HEIGHT - self.height - self.horizontal.height) // 2 + 100

        self.end_x = self.start_x + self.size_field * self.j_count_fields
        self.end_y = self.start_y + self.size_field * self.i_count_fields

        # 780 - это граница, где начинаются кнопки
        # self.start_y = (750 - self.horizontal.height - self.width) // 2
        # self.start_x = (HEIGHT - self.vertical.width - self.height) // 2 + 100

        for i in range(len(self.fields)):
            for j in range(len(self.fields[i])):
                self.fields[i][j] = Square(self.start_x + j * self.size_field,
                                           self.start_y + i * self.size_field,
                                           self.size_field)
                # Включить, чтобы при загрузке показались все квадраты
                # self.fields[i][j].enabled = self.current_map[i][j]

        self.horizontal = Horizontal(self.current_map, self.start_x, self.start_y, self.size_field, self.font)
        self.vertical = Vertical(self.current_map, self.start_x, self.start_y, self.size_field, self.font)

        # Из скольки клеток состоят обведённые светлом блоки (3x3, 4x4, 5x5)
        marker = [1, 2, 3, 4, 5]
        for i in marker:
            if len(self.fields) % i == 0:
                self.i_line_cells = i
        for j in marker:
            if len(self.fields) % j == 0:
                self.j_line_cells = j

    def getCoord(self, j, i):
        if (j < self.start_x or j >= self.end_x or
                i < self.start_y or i >= self.end_y):
            return -1, -1

        i = (i - self.start_y) // self.size_field
        j = (j - self.start_x) // self.size_field
        return j, i

    def set_blocked(self, j, i):
        j, i = self.getCoord(j, i)
        if j == -1 and i == -1:
            return False

        self.blocked = not self.fields[i][j].blocked

    def mouse_3_button_down(self, mouse, j, i):
        j, i = self.getCoord(j, i)
        if j == -1 and i == -1:
            return False
        self.fields[i][j].blocked = self.blocked

    def press_mouse_1(self, x, y):
        if not (self.vertical is None):
            self.vertical.press_mouse_1(x, y)
        if not (self.horizontal is None):
            self.horizontal.press_mouse_1(x, y)


    def act(self, deltatime, x, y):
        self.frame += 1
        if self.frame > 100000:
            self.frame = 1

        if not (self.vertical is None):
            self.vertical.check_mouse(x, y)
        if not (self.horizontal is None):
            self.horizontal.check_mouse(x, y)

        if self.frame % 30 == 0:
            for i in range(len(self.errors) - 1, -1, -1):
                if not self.errors[i].enabled:
                    del self.errors[i]

            for i in range(len(self.helper) - 1, -1, -1):
                if not self.helper[i].enabled:
                    del self.helper[i]

    # Выводит на экран содержимое всех вложенных объектов классов
    def draw(self, scene: pygame, deltatime):

        for i in range(len(self.fields)):
            for j in range(len(self.fields[i])):
                self.fields[i][j].drawIJ(scene, j, i, self.i_line_cells, self.j_line_cells)

        # Выводим анимацию ошибок
        if len(self.errors) > 0:
            for err in self.errors:
                err.draw(scene, deltatime)

        # Выводим клетки-подсказки
        if len(self.helper) > 0:
            for hlp in self.helper:
                hlp.draw(scene, deltatime)

        pygame.draw.rect(scene, Square.color_fill, (self.start_x - 1, self.start_y - 1,
                                                            self.width + 2, self.height + 2), 4)
        if not (self.vertical is None):
            self.vertical.draw(scene)
        if not (self.horizontal is None):
            self.horizontal.draw(scene)

        self.label_text.draw(scene)

    # Установка/переключатель заливки/удаления
    def set_filling(self, j, i):
        j, i = self.getCoord(j, i)
        if j == -1 and i == -1:
            return False

        self.fill = not self.fields[i][j].enabled

    # Нажатие мышкой по полю/клетке
    # Тут же считает и ошибки
    def mouse_1_button_down(self, mouse, j, i):
        j, i = self.getCoord(j, i)
        if j == -1 and i == -1:
            return False

        if self.fields[i][j].blocked:
            return False

        if mouse == 1:
            self.fields[i][j].enabled = self.fill

            if self.fill:
                if self.last_i != i or self.last_j != j:
                    self.last_i = i
                    self.last_j = j
                    if self.current_map[i][j] == 0:
                        self.errors.append(Error(self.fields[i][j], FPS / 2))
                        setup.error += 1
                        self.fields[i][j].blocked = True
                        self.fields[i][j].enabled = False
                        self.last_i = -1
                        self.last_j = -1

    # Ищет подсказки: сравнивает каждую выключенную клетку с базой
    # Если в клетке нужно установить заливку, а её нет, то устанавливает
    # Количество определяется по формуле: количество незакрашенных клеток / 3, но не менее 1
    def run_help(self):
        if len(self.helper) > 0:
            return False
        if setup.hint == 0:
            return False

        clear_fields = []

        for i in range(len(self.current_map)):
            for j in range(len(self.current_map[i])):
                if self.current_map[i][j] == 1 and self.fields[i][j].enabled == False:
                    clear_fields.append([self.fields[i][j], i, j])

        if len(clear_fields) > 0:
            setup.hint -= 1

            random.shuffle(clear_fields)
            count = min(max(len(clear_fields) // 3, 1), 3)
            for i in range(count):
                self.helper.append(Helper(clear_fields[i][0], setup.FPS // 2))
                self.fields[clear_fields[i][1]][clear_fields[i][2]].enabled = True
