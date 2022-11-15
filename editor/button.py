import pygame

class Button:
    def __init__(self, x, y, image_file):
        self.x = x
        self.y = y
        self.image_file = pygame.image.load(image_file)

    def draw(self, scene):
        scene.blit(self.image_file, (self.x, self.y))

    def is_pressed(self, x, y):
        if (x > self.x and x < self.x + self.image_file.get_width() and
        y > self.y and y < self.y + self.image_file.get_height()):
            return True
        return False



