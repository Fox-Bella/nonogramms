import pygame
from setup import *
from engine.square import Square
from engine.horizontal import Horizontal
from engine.vertical import Vertical


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
        self.start_level()

    def getCoord(self, j, i):
        if (j < self.start_x or j >= self.end_x or
                i < self.start_y or i >= self.end_y):
            return -1, -1

        i = (i - self.start_y) // self.size_field
        j = (j - self.start_x) // self.size_field
        return j, i

    def set_filling(self, j, i):
        j, i = self.getCoord(j, i)
        if j == -1 and i == -1:
            return False

        self.fill = not self.fields[i][j].enabled

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

    def mouse_1_button_down(self, mouse, j, i):
        j, i = self.getCoord(j, i)
        if j == -1 and i == -1:
            return False
        if mouse == 1:
            self.fields[i][j].enabled = self.fill

    def start_level(self):
        # Текущая карта
        self.current_map = self.maps.level[level].data_level
        # Текущая карта с True или False
        # Самое коряво написанное, но быстрое копирование в Python
        self.fields = [f[:] for f in self.current_map]

        self.size_field = square_game_sizes[min(len(self.fields), len(self.fields[0])) - 1]

        self.start_x = (WIDTH - len(self.current_map[0]) * self.size_field) // 2
        self.start_y = (HEIGHT - len(self.current_map) * self.size_field) // 2 + 50
        self.i_count_fields = len(self.current_map)
        self.j_count_fields = len(self.current_map[0])
        self.end_x = self.start_x + self.size_field * self.j_count_fields
        self.end_y = self.start_y + self.size_field * self.j_count_fields

        for i in range(len(self.fields)):
            for j in range(len(self.fields[i])):
                self.fields[i][j] = Square(self.start_x + j * self.size_field,
                                           self.start_y + i * self.size_field,
                                           self.size_field)
                # Включить, чтобы при загрузке показались все квадраты
                # self.fields[i][j].enabled = self.current_map[i][j]

        marker = [3, 4, 5]
        for i in marker:
            if len(self.fields) % i == 0:
                self.i_line_cells = i
        for j in marker:
            if len(self.fields) % j == 0:
                self.j_line_cells = j

        self.horizontal = Horizontal(self.current_map, self.start_x, self.start_y, self.size_field)
        self.vertical = Vertical(self.current_map, self.start_x, self.start_y, self.size_field)


    def draw(self, scene: pygame, deltatime):
        for i in range(len(self.fields)):
            for j in range(len(self.fields)):
                self.fields[i][j].drawIJ(scene, j, i, self.i_line_cells, self.j_line_cells)

        if not (self.vertical is None):
            self.vertical.draw(scene)
        if not (self.horizontal is None):
            self.horizontal.draw(scene)

    def act(self, deltatime, x, y):
        if not (self.vertical is None):
            self.vertical.check_mouse(x, y)
        if not (self.horizontal is None):
            self.horizontal.check_mouse(x, y)

    def press_mouse_1(self, x, y):
        if not (self.vertical is None):
            self.vertical.press_mouse_1(x, y)
        if not (self.horizontal is None):
            self.horizontal.press_mouse_1(x, y)