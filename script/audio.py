import pygame
from Jeu import Jeu

class sound:
    def __init__(self):
        self.jeu = Jeu()
        pygame.mixer.music.load("audio/tetris.mp3")
        pygame.mixer.music.play(loops=-1)