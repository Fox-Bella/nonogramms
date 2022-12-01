import pygame
from setup import *


class StartScreen:

    def __init__(self):
        self.frame = 0
        self.enabled = True
        self.alpha = 255
        self.img = pygame.image.load("png/skanmatic.png")

    def draw(self, scene, deltatime):

        if self.frame < FPS * 1.5:
            self.frame += 1
        else:
            self.alpha -= 255 * deltatime / 2

        self.img.set_alpha(self.alpha)
        scene.blit(self.img, (0, 0))