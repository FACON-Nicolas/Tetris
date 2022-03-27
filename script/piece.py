from cmath import sqrt
import random
from typing import List


class Piece:

    row = 0
    col = 0

    def __init__(self, tab):
        """ write docstrings """
        self.__tab = tab
        self.__numTab = 0

    @staticmethod
    def resetPos(row: int, col: int):
        """ write docstrings """
        Piece.row, Piece.col = row, col

    @staticmethod 
    def goLeft(): 
        """ write docstrings """
        if Piece.col > 0: Piece.col -= 1

    @staticmethod
    def goRight(leng: int):
        """ write docstrings """ 
        if Piece.col < leng: Piece.col += 1

    @staticmethod
    def goDown():
        """ write docstrings """
        Piece.row += 1

    def getNumTab(self):
        """ write docstrings """
        return self.__numTab

    def getTab(self):
        """ write docstrings """
        return self.__tab

    def getTabWithIndex(self):
        """ write docstrings """
        return self.__tab[self.getNumTab()]

    def getNextNumTab(self):
        """ write docstrings """
        return (self.getNumTab()+1)%(len(self.__tab))

    def pivotPiece(self):
        """ write docstrings """
        self.__numTab = self.getNextNumTab()