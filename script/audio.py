import pygame

class sound:
    def __init__(self):
        pygame.mixer.music.load("audio/tetris.mp3")
        pygame.mixer.music.play(loops=-1)