from typing import List
from piece import Piece

class Jeu:
    """ permet de reunir en une classe 
     des fonctionnalites du Tetris """
    def __init__(self):
        """ initialisation du jeu """
        self.game_running = True
        self.isDown = False
        self.Touches = list()
