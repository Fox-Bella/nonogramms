import pygame


class FinalText:

    def __init__(self, msg1, msg2, name_image, font, left_x, right_x):
        self.msg1 = font.getBigText("MSG1", msg1, "#dd9587")
        self.msg2 = font.getSmallText("MSG2", msg2, "#AAAA99")

        self.msg1_x = (right_x - left_x - self.msg1.get_width()) // 2
        self.msg2_x = (right_x - left_x - self.msg2.get_width()) // 2

        self.alpha = 0

        self.font = font
        self.img = pygame.image.load(name_image)
        self.img_x = (right_x - left_x - self.img.get_width()) // 2

    def draw(self, scene: pygame.Surface, deltatime):

        if self.alpha < 255:
            self.alpha += 125 * deltatime
            if self.alpha > 255:
                self.alpha = 255

        self.msg1.set_alpha(int(self.alpha))
        self.msg2.set_alpha(int(self.alpha))
        self.img.set_alpha(int(self.alpha))

        scene.blit(self.msg1, (self.msg1_x, 100))
        scene.blit(self.msg2, (self.msg2_x, 620))

        scene.blit(self.img, (self.img_x, 250))
