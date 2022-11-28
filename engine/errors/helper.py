import pygame
from engine.square import Square


class Helper:

    def __init__(self, field: Square, max_frame, pause=0, r=0, g=0, b=0):
        self.size = field.size
        self.x = field.x  # + field.size // 2
        self.y = field.y  # + field.size // 2
        self.size = field.size - 4  # // 2
        self.enabled = True
        self.max_frame = max_frame
        self.current_frame = 0
        self.pause = pause

        self.r = r
        self.g = g
        self.b = b

    def draw(self, scene, deltatime):
        self.current_frame += 1

        if self.pause > self.current_frame:
            return False

        if self.current_frame - self.pause > self.max_frame:
            self.enabled = False

        if self.enabled:
            pygame.draw.rect(scene,
                             (int(self.r), int(self.g), int(self.b)),
                             (self.x + 2, self.y + 2, self.size, self.size))
            pygame.draw.rect(scene,
                             Square.color_line_outline,
                             (self.x + 4, self.y + 4, self.size - 4, self.size - 4), 2)

            # self.r += deltatime * 512
            self.g += deltatime * 350
            self.b += deltatime * 5

            if self.r > 255:
                self.r = 0
            if self.g > 255:
                self.g = 0
            if self.b > 255:
                self.b = 0
