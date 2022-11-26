from engine.vertical import Vertical
from engine.data_lines import DataLines
import random
import setup


class Horizontal(Vertical):

    def __init__(self, maps, start_x, start_y, size_cell, font):
        # for y in range(len(maps)):
        #     for x in range(len(maps[y])):
        #         print(f"{maps[y][x]} ", end="")
        #     print()

        self.data_lines = []
        self.font = font
        mx = 0
        for x in range(len(maps)):
            count = 0
            data = []
            for y in range(len(maps[0])):
                count += maps[x][y]
                if maps[x][y] == 0 and count > 0:
                    data.append(count)
                    count = 0
            if count > 0:
                data.append(count)
            # print(data)
            self.data_lines.append(DataLines(start_x - size_cell,
                                             start_y + size_cell * x + (size_cell - 23) // 2,
                                             size_cell, data,
                                             font,
                                             setup.TEXT_COLOR[x % 2],
                                             DataLines.HORIZONTAL))
            if len(data) > mx:
                mx = len(data)

        self.height = mx * size_cell

        # Сделать нужное количество значений чисел выражениями
        self.set_expression_digit()
