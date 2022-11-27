from engine.data_lines import DataLines
import setup
import random

class Vertical:

    def __init__(self, maps, start_x, start_y, size_cell, font):
        # for y in range(len(maps)):
        #     for x in range(len(maps[y])):
        #         print(f"{maps[y][x]} ", end="")
        #     print()

        self.data_lines = []
        self.font = font

        mx = 0
        for x in range(len(maps[0])):
            count = 0
            data = []
            for y in range(len(maps)):
                count += maps[y][x]
                if maps[y][x] == 0 and count > 0:
                    data.append(count)
                    count = 0
            # if count > 0 or (count == 0 and len(data) == 0):
            #     data.append(count)
            if count > 0:
                data.append(count)

            # print(data)
            self.data_lines.append(DataLines(start_x + x * size_cell,
                                             start_y - 30, size_cell,
                                             data,
                                             font,
                                             setup.TEXT_COLOR[x % 2],
                                             DataLines.VERTICAL))

            if len(data) > mx:
                mx = len(data)

        self.width = mx * size_cell

        # Сделать нужное количество значений чисел выражениями
        self.set_expression_digit()

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

    def set_expression_digit(self):
        tmp = []
        for dtl in self.data_lines:
            for cell in dtl.cells:
                tmp.append(cell)

        count = int(len(tmp) / 100 * setup.percent_digits[setup.difficulty])
        # print(f"Количество: {len(tmp)} + {count} штук + diff: {setup.difficulty}")

        #tmp = self.cells[:]
        random.shuffle(tmp)
        for i in range(count):
            tmp[i].set_error_digit()

        #self.cells = tmp