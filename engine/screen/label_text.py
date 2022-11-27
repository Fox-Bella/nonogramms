import pygame
import setup
from engine.square import Square



class LabelText:

    def __init__(self, font):
        self.font = font

    def draw(self, scene: pygame.surface):
        scene.blit(self.font.getSystemText("ERROR", f"Ошибки: {setup.error}", setup.TEXT_COLOR[0]), (10, 10))
        scene.blit(self.font.getSystemText("LEVEL", f"Уровень: {setup.level + 1}", setup.TEXT_COLOR[0]), (260, 10))
        scene.blit(self.font.getSystemText("HINT", f"Подсказки: {setup.hint}", setup.TEXT_COLOR[0]), (530, 10))
        scene.blit(self.font.getSystemText("MAX_LEVEL", f"Пройдено: {setup.max_level}", setup.TEXT_COLOR[0]), (830, 10))