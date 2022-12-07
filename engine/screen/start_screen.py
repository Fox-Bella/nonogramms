import pygame
from setup import *


class StartScreen:

    def __init__(self):
        self.frame = 0
        self.enabled = True
        self.alpha = 255
        self.img = pygame.image.load("png/skanmatic.png")
        self.enabled = True

    def draw(self, scene, deltatime):
        if self.enabled:

            # УДАЛИТЬ
            # self.alpha -= 2255 * deltatime / 2

            if self.frame < FPS * 1.5:
                self.frame += FPS * deltatime
            else:
                self.alpha -= 255 * deltatime / 2

            if self.alpha <= 0:
                self.enabled = False

            self.img.set_alpha(self.alpha)
            scene.blit(self.img, (0, 0))
