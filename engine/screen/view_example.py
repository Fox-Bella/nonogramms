import pygame
import setup
from engine.font import Font
from engine.square import Square
from random import randint


class ViewExample:
    class Button:

        def __init__(self, x, y, width, height, font, value):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.font = font
            self.value = value

        def draw(self, scene):
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            if self.x < x < self.x + self.width and \
                    self.y < y < self.y + self.height:
                pygame.draw.rect(scene, setup.TEXT_LIGHT_GOOD, (self.x, self.y, self.width, self.height))
                pygame.draw.rect(scene, Square.color_fill, (self.x, self.y, self.width, self.height), 2)
                scene.blit(self.font.getBigText(f"BTN{self.value}", f"{self.value}", setup.COLOR_WHITE),
                           (self.x + 9, self.y + 2))
            else:
                pygame.draw.rect(scene, Square.color, (self.x, self.y, self.width, self.height))
                pygame.draw.rect(scene, Square.color_fill, (self.x, self.y, self.width, self.height), 2)
                scene.blit(self.font.getBigText(f"BTN{self.value}", f"{self.value}", setup.COLOR_WHITE),
                           (self.x + 9, self.y + 2))


        def press_mouse(self, x, y):
            if self.x < x < self.x + self.width and \
                    self.y < y < self.y + self.height:
                return f"{self.value}"
            return False

    def __init__(self, x, y, size_field, value, cell):
        self.x = x + size_field
        self.y = y
        self.size_field = size_field
        self.value = value
        self.cell = cell

        self.font = Font()
        self.msg = ""
        self.frame = 0
        self.data_input = ""

        if value > 4 and randint(0, 100) < 50:
            n = randint(1, value)
            self.msg = f"{n} + {value - n} = "
        else:
            n = randint(value + 1, 10 + value ** 2)
            self.msg = f"{n} - {n - value} = "

        self.width = 375
        self.height = 180
        self.x -= self.width // 4 + size_field
        self.y -= self.height // 4 + size_field

        if self.y + self.height + 20 > setup.HEIGHT:
            self.y = self.height + self.height + 20
        if self.y - self.height - 20 <= 0:
            self.y = 20
        if self.x + self.width + 20 >= setup.WIDTH:
            self.x = setup.WIDTH - self.width - 20

        if self.x < 20:
            self.x = 20

        self.buttons = []
        for i in range(10):
            self.buttons.append(self.Button(self.x + 15 + i * 35, self.y + 100, 30, 30, self.font, i))
        self.buttons.append(self.Button(self.x + 15, self.y + 135, 53, 30, self.font, "<<<"))
        self.buttons.append(self.Button(self.x + 73, self.y + 135, 73, 30, self.font, "Ввод"))

    def draw(self, scene):
        self.frame += 1

        if self.frame < setup.FPS // 2:
            cursor = "|"
        else:
            cursor = ""

        if self.frame > setup.FPS:
            self.frame = 0

        pygame.draw.rect(scene, Square.color_line, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(scene, Square.color_fill, (self.x, self.y, self.width, self.height), 5)
        scene.blit(self.font.getBigText("CAPTION", "Решите пример:", setup.COLOR_WHITE), (self.x + 15, self.y + 10))
        scene.blit(self.font.getBigText("EXAMPLE", self.msg + self.data_input + cursor, setup.COLOR_YELLOW),
                   (self.x + 15, self.y + 50))

        for i in range(len(self.buttons)):
            self.buttons[i].draw(scene)

    def press_mouse_button_1(self, x, y):
        for b in self.buttons:
            pm = b.press_mouse(x, y)
            if pm != False:
                if self.data_input == "" and pm == "0":
                    return False
                elif pm == "<<<":
                    if len(self.data_input) > 0:
                        self.data_input = self.data_input[:-1]
                elif pm == "Ввод":
                    self.enter(self.data_input, False)
                else:
                    if len(self.data_input) == 2:
                        self.data_input = self.data_input[:-1]
                    self.data_input += pm

        if len(self.data_input) > 0:
            if self.data_input == f"{self.cell.value}":
                self.enter(self.data_input, True)

        return True

    def enter(self, n, b):
        if n == "":
            self.cell.delete_view_example()
        else:
            self.cell.print_to_screen = n
            if b:
                self.cell.error_digit = False
        self.cell.delete_view_example()
