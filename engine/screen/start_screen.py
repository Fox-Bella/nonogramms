import pygame


class StartScreen:

    def __init__(self):
        self.enabled = True
        self.alpha = 255
        self.img = pygame.image.load("png/skanmatic.png")

    def draw(self, scene, deltatime):

        self.img.set_alpha(self.alpha)
        scene.blit(self.img, (0, 0))

        self.alpha -= 255 * deltatime / 2