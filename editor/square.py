import pygame
import setup
class Square:

    color = (100, 100, 100)
    color_line = (190, 190, 190)
    color_fill = (170, 170, 170)

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.enabled = False

    def draw(self, scene: pygame):
        if self.enabled:
            pygame.draw.rect(scene, Square.color_fill, (self.x + 3, self.y + 3, self.size - 6, self.size - 6))
        else:
            pygame.draw.rect(scene, Square.color, (self.x, self.y, self.size, self.size), 1)

        if ((self.x - setup.BLANK_FIELD) / self.size) % 5 == 0:
            pygame.draw.line(scene, Square.color_line, (self.x, self.y), (self.x, self.y + self.size), 2)
        elif ((self.x + self.size - setup.BLANK_FIELD) / self.size) % 5 == 0:
            pygame.draw.line(scene, Square.color_line, (self.x + self.size, self.y), (self.x + self.size, self.y + self.size), 2)

        if ((self.y - setup.BLANK_FIELD) / self.size) % 5 == 0:
            pygame.draw.line(scene, Square.color_line, (self.x, self.y), (self.x + self.size, self.y), 2)
        elif ((self.y + self.size - setup.BLANK_FIELD) / self.size) % 5 == 0:
            pygame.draw.line(scene, Square.color_line, (self.x, self.y + self.size), (self.x + self.size, self.y + self.size), 2)





