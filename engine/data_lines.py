from engine.cell import Cell
from engine.font import Font
from setup import *

class DataLines:

    VERTICAL = 0
    HORIZONTAL = 1

    def __init__(self, x, y, size, line, color, type):
        self.x = x
        self.y = y
        self.size = size
        self.font = Font()
        self.color = color
        self.type = type

        self.cells = []
        if type == DataLines.VERTICAL:
            print(line)
            for i in range(len(line)):
                self.cells.append(Cell(line[len(line) - i - 1], self.x, self.y - 30 * i, self.size, self.font, self.color))
        elif type == DataLines.HORIZONTAL:
            for i in range(len(line)):
                self.cells.append(Cell(line[len(line) - i - 1], self.x - max(20 * i, self.size // 1.4 * i), self.y, self.size // 1.4, self.font, self.color))

    def check_mouse(self, x, y):
        for i in range(len(self.cells)):
            self.cells[i].check_mouse(x, y)

    def draw(self, scene):
        for i in range(len(self.cells)):
            self.cells[len(self.cells) - i - 1].draw(scene)

    def press_mouse_1(self, x, y):
        for i in range(len(self.cells)):
            self.cells[len(self.cells) - i - 1].press_mouse_1(x, y)