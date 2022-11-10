import pygame
from square import Square
import setup
from random import randint

class Manager:

    def __init__(self):
        self.sq = []
        for i in range(20):
            self.sq.append([])
            for j in range(20):
                self.sq[i].append(Square(64 + i * setup.SIZE, 64 + j * setup.SIZE, setup.SIZE))

    def draw(self, scene: pygame):
        for i in range(len(self.sq)):
            for j in range(len(self.sq[i])):
                self.sq[i][j].draw(scene)

    def click(self, x, y):
        p1 = (x - 64) // setup.SIZE
        p2 = (y - 64) // setup.SIZE
        self.sq[p1][p2].enabled = not self.sq[p1][p2].enabled