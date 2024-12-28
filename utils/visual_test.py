import pygame

class LineTest():
    def __init__(self):
        pass

    @staticmethod
    def drawLine(window, x1, x2, y1, y2):
        pygame.draw.line(window, (255,0,0), (x1, y1), (x2, y2), 5)