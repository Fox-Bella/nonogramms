import pygame
import setup

class PlayTxt:

    def __init__(self, font):
        self.font = font
        self.txt = []
        self.txt.append("Как играть?")
        self.txt.append("")
        self.txt.append("Что это за кнопка с вопросом?")
        self.txt.append("С помощью этой кнопки надо разгадывать число (в строке или столбце)")
        self.txt.append("")
        self.txt.append("Как проходить уровни?")
        self.txt.append("Нужно смотреть на число в начале строки или вверху столбца сколько там чисел столько")
        self.txt.append("закрашеных клеток в строке. Если есть цифра ,а потом ещё цифра это значит что есть")
        self.txt.append("некоторое количество закрашеных клеток (сколько написано), потом пропуск (может быть")
        self.txt.append("более 1 клетки), а потом другое количество закрашеных клеток (сколько написано). Если")
        self.txt.append("в начале или верху строки ничего не написано значит там нету зарашеных клеток.")

        self.x = 900

    def draw(self, scene: pygame.surface, deltatime):

        pygame.draw.rect(scene, (37, 37, 37), (self.x, 150, 1000, 430))
        if self.x > 200:
            self.x -= 2000 * deltatime

        for i in range(len(self.txt)):
            if i == 0:
                clr = setup.COLOR_YELLOW
                surftext = self.font.getMediumText(f"PL{i}", self.txt[i], clr)
            else:
                clr = setup.COLOR_GRAY
                surftext = self.font.getSmallText(f"PL{i}", self.txt[i], clr)

            # x = (setup.WIDTH - surftext.get_width()) // 2
            scene.blit(surftext, (self.x + 30, 220 + 30 * i))
