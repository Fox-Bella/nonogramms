import pygame
import setup

class AuthorsText:

    def __init__(self, font):
        self.font = font
        self.txt = []
        self.txt.append("СКАН-МАТИК / Японские сканворды с математикой")
        self.txt.append("")
        self.txt.append("Идея игры и фигуры:")
        self.txt.append("Евгения Рябухо (с) 2022")
        self.txt.append("")
        self.txt.append("Программирование и дизайн:")
        self.txt.append("Евгения Рябухо, Виктор Трофимов (с) 2022")
        self.txt.append("")
        self.txt.append("Успехов вам!")

        self.x = 900

    def draw(self, scene: pygame.surface, deltatime):

        pygame.draw.rect(scene, (37, 37, 37), (self.x, 150, 1000, 400))
        if self.x > 200:
            self.x -= 2000 * deltatime

        for i in range(len(self.txt)):
            if i == 0:
                clr = setup.COLOR_YELLOW
                surftext = self.font.getMediumText(f"AUTH{i}", self.txt[i], clr)
            else:
                clr = setup.COLOR_GRAY
                surftext = self.font.getSmallText(f"AUTH{i}", self.txt[i], clr)

            # x = (setup.WIDTH - surftext.get_width()) // 2
            scene.blit(surftext, (self.x + 40, 220 + 30 * i))

