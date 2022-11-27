import pygame
from engine.square import Square


class Helper:

    def __init__(self, field: Square, max_frame):
        self.size = field.size
        self.x = field.x  # + field.size // 2
        self.y = field.y  # + field.size // 2
        self.size = field.size - 4  # // 2
        self.enabled = True
        self.max_frame = max_frame
        self.current_frame = 0

        self.r = 0
        self.g = 0
        self.b = 0

    def draw(self, scene, deltatime):
        self.current_frame += 1

        if self.current_frame > self.max_frame:
            self.enabled = False

        if self.enabled:
            pygame.draw.rect(scene,
                             (int(self.r), int(self.g), int(self.b)),
                             (self.x + 2, self.y + 2, self.size, self.size))
            pygame.draw.rect(scene,
                             Square.color_line_outline,
                             (self.x + 2, self.y + 2, self.size, self.size), 2)

            # self.r += deltatime * 512
            self.g += deltatime * 250
            self.b += deltatime * 50

            if self.r > 255:
                self.r = 0
            if self.g > 255:
                self.g = 0
            if self.b > 255:
                self.b = 0
