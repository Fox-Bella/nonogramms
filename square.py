import pygame
class Square:

    color = (100, 100, 100)
    color_fill = (170, 170, 170)

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.enabled = False

    def draw(self, scene: pygame):
        if (self.enabled):
            pygame.draw.rect(scene, Square.color_fill, (self.x + 3, self.y + 3,
                                                   self.size - 6, self.size - 6))
        else:
            pygame.draw.rect(scene, Square.color, (self.x, self.y, self.size, self.size), 1)

