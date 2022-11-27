import setup
import pygame


class LabelTextCentral:

    # size 2 или 1 - большой или поменьше размер шрифта
    def __init__(self, y, text, id, color, font, max_frame, size):

        self.text = text
        if size == 2:
            self.surface_text = font.getBigText(id, text, color)
        elif size == 1:
            self.surface_text = font.getMediumText(id, text, color)

        self.x = (setup.WIDTH - self.surface_text.get_width()) // 2
        self.y = y
        self.enabled = True
        self.max_frame = max_frame
        self.frame = 0
        self.alpha = 0
        self.increment_alpha = 1024

    def draw(self, scene: pygame.Surface, deltatime):
        if self.enabled:
            self.surface_text.set_alpha(self.alpha)

            if self.frame > self.max_frame * 0.6:
                self.alpha -= self.increment_alpha * deltatime
            else:
                self.alpha += self.increment_alpha * deltatime

            if self.alpha < 0:
                self.alpha = 0
            elif self.alpha > 255:
                self.alpha = 255

            scene.blit(self.surface_text, (self.x, self.y))
            self.frame += 1
            if self.frame > self.max_frame:
                self.enabled = False
