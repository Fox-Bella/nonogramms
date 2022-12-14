import pygame
from square import Square
import setup
from button import Button
from getcode import GetCode


class Manager:

    def __init__(self):
        self.sq = []
        self.trigger = False
        for i in range(20):
            self.sq.append([])
            for j in range(20):
                self.sq[i].append(Square(setup.BLANK_FIELD + i * setup.SIZE,
                                         setup.BLANK_FIELD + j * setup.SIZE,
                                         setup.SIZE))

        self.get_code_button = Button(578, 757, '../png/button_get.png')
        self.clear_button = Button(64, 757, '../png/button_delete.png')

    def draw(self, scene: pygame):
        for i in range(len(self.sq)):
            for j in range(len(self.sq[i])):
                self.sq[i][j].drawIJ(scene, setup.BLANK_FIELD + i * setup.SIZE, setup.BLANK_FIELD + j * setup.SIZE)
                # self.sq[i][j].draw(scene)

        self.get_code_button.draw(scene)
        self.clear_button.draw(scene)

    def get_xy_coordinate_from_mouse(self, x, y):
        p1 = (x - setup.BLANK_FIELD) // setup.SIZE
        p2 = (y - setup.BLANK_FIELD) // setup.SIZE
        return p1, p2

    def click(self, x, y):
        p1, p2 = self.get_xy_coordinate_from_mouse(x, y)
        if (p1 >= 0 and p1 < len(self.sq) and p2 >= 0 and p2 < len(self.sq[0])):
            self.sq[p1][p2].enabled = self.trigger

    def newMotion(self, x, y):
        p1, p2 = self.get_xy_coordinate_from_mouse(x, y)

        if (self.get_code_button.is_pressed(x, y)):
            GetCode().get_code(self.sq)

        if (self.clear_button.is_pressed(x, y)):
            for i in range(len(self.sq)):
                for j in range(len(self.sq[i])):
                    self.sq[i][j].enabled = False


        # print(x, y)

        if (p1 >= 0 and p1 < len(self.sq) and p2 >= 0 and p2 < len(self.sq[0])):
            self.trigger = not self.sq[p1][p2].enabled

    # Вернёт True, если клетка закрашена
    def getEnabled(self, x, y):
        p1, p2 = self.get_xy_coordinate_from_mouse(x, y)
        if (p1 >= 0 and p1 < len(self.sq) and p2 >= 0 and p2 < len(self.sq[0])):
            return self.sq[p1][p2].enabled