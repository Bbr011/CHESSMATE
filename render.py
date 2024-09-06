import pygame

from values import *


class Game():
    def __init__(self):
        pass

    def render_bg(self, surface):
        for r in range(ROWS):
            for c in range(COLS):
                if (r + c) % 2 == 0:
                    color = (234, 235, 200)
                else:
                    color = (119, 154, 88)
                    
                rect = (c * SQSIZE, r * SQSIZE, SQSIZE, SQSIZE)
                
                pygame.draw.rect(surface, color, rect)