from cmath import sqrt
import random
from typing import List


class Piece:

    row = 0
    col = 0

    def __init__(self, tab):
        self.__tab = tab
        self.__numTab = 0

    @staticmethod
    def resetPos(row: int, col: int):
        Piece.row, Piece.col = row, col

    def goToFinalPosition(self): pass

    @staticmethod 
    def goLeft(): 
        if Piece.col > 0: Piece.col -= 1

    @staticmethod
    def goRight(leng: int): 
        if Piece.col < leng: Piece.col += 1

    @staticmethod
    def goDown():
        Piece.row += 1

    def getNumTab(self):
        return self.__numTab

    def getTab(self):
        return self.__tab

    def getTabWithIndex(self):
        return self.__tab[self.getNumTab()]

    def getNextNumTab(self):
        return (self.getNumTab()+1)%(len(self.__tab))

    def pivotPiece(self):
        self.__numTab = self.getNextNumTab()
        print(self.__numTab)