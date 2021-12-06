from typing import List

class Jeu:
    """ permet de reunir en une classe 
     des fonctionnalites du Tetris """
    def __init__(self):
        """ initialisation du jeu """
        self.game_running = True
        self.isDown = False
        self.isInGame = True
        self.isGamePaused = False
        self.Touches = list()
        self.compteur = 0
        self.vitesse = 60
