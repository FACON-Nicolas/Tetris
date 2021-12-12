import pygame
from Jeu import Jeu

class sound:
    def __init__(self):
        self.jeu = Jeu()
        self.theme = self.jeu.path+"audio\\tetris.mp3"
        pygame.mixer.music.load(self.theme)
        pygame.mixer.music.play(loops=-1)
