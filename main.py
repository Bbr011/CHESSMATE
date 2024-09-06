import pygame
import sys

from values import *
from render import Game


class Main():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("CHESSMATE")
        self.render = Game()
            
    def mainloop(self):
        screen = self.screen
        render = self.render
        while True:
            render.render_bg(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            pygame.display.update()
    
main = Main()
main.mainloop()