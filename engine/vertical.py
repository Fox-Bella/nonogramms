from engine.data_lines import DataLines
from setup import *

class Vertical:

    def __init__(self, maps, start_x, start_y, size_cell):
        # for y in range(len(maps)):
        #     for x in range(len(maps[y])):
        #         print(f"{maps[y][x]} ", end="")
        #     print()

        self.data_lines = []

        for x in range(len(maps[0])):
            count = 0
            data = []
            for y in range(len(maps)):
                count += maps[y][x]
                if maps[y][x] == 0 and count > 0:
                    data.append(count)
                    count = 0
            if count > 0:
                data.append(count)
            # print(data)
            self.data_lines.append(DataLines(start_x + x * size_cell, start_y - 30, size_cell, data, TEXT_COLOR[x % 2]))

    def check_mouse(self, x, y):
        for i in range(len(self.data_lines)):
            self.data_lines[i].check_mouse(x, y)

    def draw(self, scene):
        for i in range(len(self.data_lines)):
            self.data_lines[i].draw(scene)

    # Нажата кнопка мыши для активации примера
    def press_mouse_1(self, x, y):
        for i in range(len(self.data_lines)):
            self.data_lines[i].press_mouse_1(x, y)