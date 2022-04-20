
import pygame
from GUI import *
from random import randint, choice
from piece import Piece
from math import sqrt
from Color import Color
from typing import List


class Display:
    """ TODO: write docstring """

    WIDTH_WINDOW = 1000
    HEIGHT_WINDOW = 660

    WIDTH_PLATFORM = 11
    HEIGHT_PLATFORM = 22

    CASE_WIDTH = 30

    TIME_DELTA = 1

    I = [[0,2,0,0,2,0,0,2,0],[0,0,0,2,2,2,0,0,0],[0,2,0,0,2,0,0,2,0],[0,0,0,2,2,2,0,0,0]]
    T = [[0,0,0,4,4,4,0,4,0],[0,4,0,0,4,4,0,4,0],[0,4,0,4,4,4,0,0,0],[0,4,0,4,4,0,0,4,0]]
    J = [[0,0,0,5,5,5,0,0,5],[0,5,0,0,5,0,5,5,0],[5,0,0,5,5,5,0,0,0],[0,5,5,0,5,0,0,5,0]]
    L = [[0,0,0,6,6,6,6,0,0],[0,6,0,0,6,0,0,6,6],[0,0,6,6,6,6,0,0,0],[6,6,0,0,6,0,0,6,0]]
    Z = [[0,0,0,8,8,0,0,8,8],[0,8,0,8,8,0,8,0,0],[0,0,0,8,8,0,0,8,8],[0,8,0,8,8,0,8,0,0]]
    S = [[0,0,0,0,7,7,7,7,0],[7,0,0,7,7,0,0,7,0],[0,0,0,0,7,7,7,7,0],[7,0,0,7,7,0,0,7,0]]
    O = [[3,3,0,3,3,0,0,0,0],[3,3,0,3,3,0,0,0,0],[3,3,0,3,3,0,0,0,0],[3,3,0,3,3,0,0,0,0]]

    P_I = Piece(I)
    P_T = Piece(T)
    P_L = Piece(L)
    P_J = Piece(J)
    P_Z = Piece(Z)
    P_S = Piece(S)
    P_O = Piece(O)

    def __init__(self):
        """ TODO: write docstring """
        pygame.init()
        pygame.display.set_caption('Tetris')
        self.__score = 0
        self.__surface = pygame.display.set_mode((Display.WIDTH_WINDOW, Display.HEIGHT_WINDOW), pygame.RESIZABLE)
        self.__platform = Display.initializePlatform()
        self.__piece = self.choiceNextPiece()
        self.__nextPiece = self.choiceNextPiece()
        self.__MAIN_GUI = GUI_UnPause(Display.WIDTH_WINDOW, Display.HEIGHT_WINDOW, self)
        self.__PAUSE_GUI = GUI_Pause(Display.WIDTH_WINDOW, Display.HEIGHT_WINDOW)
        self.__OVER_GUI = GUI_GameOver(Display.WIDTH_WINDOW, Display.HEIGHT_WINDOW, self)

    @staticmethod
    def initializePlatform():
        """ TODO: write docstring """
        return [[1 if row in (0, Display.HEIGHT_PLATFORM-1) or col in (0, Display.WIDTH_PLATFORM-1) else 0 \
            for col in range(Display.WIDTH_PLATFORM)] for row in range(Display.HEIGHT_PLATFORM)]

    def drawColorCase(self, row: int , col: int, case: int):
        """ write docstrings """
        color = Color.BLACK
        if case == 1: color = Color.GREY
        elif case == 2: color = Color.BLUE
        elif case == 3: color = Color.YELLOW
        elif case == 4: color = Color.PURPLE
        elif case == 5: color = Color.DARK_BLUE
        elif case == 6: color = Color.ORANGE
        elif case == 7: color = Color.RED
        elif case == 8: color = Color.GREEN
        pygame.draw.rect(self.__surface, color, (col*Display.CASE_WIDTH, \
            row*Display.CASE_WIDTH, Display.CASE_WIDTH-1, Display.CASE_WIDTH-1))

    def showPlatform(self): 
        """ TODO: write dostrings """
        self.__surface.fill((50, 50, 50))
        for row in range(len(self.__platform)):
            for col in range(len(self.__platform[0])):
                self.drawColorCase(row, col, self.__platform[row][col])

    def listOfPieces(self):
        return [Display.P_I, Display.P_T, Display.P_L, Display.P_J, Display.P_Z, Display.P_S, Display.P_O]

    def choiceNextPiece(self):
        """ TODO: write docstrings """
        return choice(self.listOfPieces())

    def changePiece(self):
        """ write docstrings """
        self.__piece.resetPos(0, Display.WIDTH_PLATFORM//2)
        self.__piece = self.__nextPiece
        self.__nextPiece = self.choiceNextPiece()

    def erasePiece(self):
        """ write docstrings """
        for i in range(len(self.__piece.getTabWithIndex())):
            row = int(self.__piece.row+(i//sqrt(len(self.__piece.getTabWithIndex()))))
            col = int(self.__piece.col+(i%sqrt(len(self.__piece.getTabWithIndex()))))
            if 0 not in (self.__platform[row][col], self.__piece.getTabWithIndex()[i]) and \
                self.__platform[row][col] == self.__piece.getTabWithIndex()[i]: self.__platform[row][col] = 0

    def changeTopWall(self):
        """ write docstrings """
        for i in range(1, Display.WIDTH_PLATFORM-1):
            self.__platform[0][i]=1 if self.__platform[0][i] == 0 else 0

    def placePiece(self, horizontalValue, verticalValue, piece=None):
        """ write docstrings """
        if piece is None: piece = self.__piece.getTabWithIndex()
        if(self.canPlacePiece(horizontalValue, verticalValue)):
            for i in range(len(piece)):
                row = int(verticalValue+(i//sqrt(len(piece))))
                col = int(horizontalValue+(i%sqrt(len(piece))))
                self.__platform[row][col] = self.__platform[row][col] if self.__platform[row][col] != 0 else piece[i]

    def canPlacePiece(self, horizontalValue: int, verticalValue: int, piece=None):
        """ write docstrings """
        if piece is None: piece = self.__piece.getTabWithIndex()
        if verticalValue == 0: self.changeTopWall()
        for i in range(len(piece)):
            row = int(verticalValue+(i//sqrt(len(piece))))
            col = int(horizontalValue+(i%sqrt(len(piece))))
            if self.__platform[row][col] != 0 and piece[i] != 0: 
                if verticalValue==0: self.changeTopWall()
                return False
        if verticalValue == 0: self.changeTopWall()
        return True

    def resizeGame(self, width: int, height=0):
        """ write docstrings """
        Display.WIDTH_WINDOW = width
        Display.HEIGHT_WINDOW = height if height else int(width*0.66)-(int(width*0.66)%Display.HEIGHT_PLATFORM)
        Display.CASE_WIDTH = int(Display.HEIGHT_WINDOW/Display.HEIGHT_PLATFORM)
        self.__surface = pygame.display.set_mode((Display.WIDTH_WINDOW, Display.HEIGHT_WINDOW), pygame.RESIZABLE)

    def setFullScreen(self):
        """ write docstrings """
        info = pygame.display.Info()
        self.resizeGame(info.current_w, info.current_h)

    def spawnPiece(self):
        """ write docstrings """
        self.changePiece()
        self.__piece.resetPos(0, randint(0, Display.WIDTH_PLATFORM-(1+sqrt(len(self.__piece.getTabWithIndex())))))
        self.placePiece(Piece.col, Piece.row)
        
    def moveLeft(self):
        """ write docstrings """
        self.erasePiece()
        if self.canPlacePiece(Piece.col-1, Piece.row): Piece.goLeft()
        self.placePiece(Piece.col, Piece.row)

    def moveRight(self):
        """ write docstrings """
        self.erasePiece()
        if (Piece.col + sqrt(len(self.__piece.getTabWithIndex())) < Display.WIDTH_PLATFORM and self.canPlacePiece(Piece.col+1, Piece.row)):
            Piece.goRight(Display.WIDTH_PLATFORM - sqrt(len(self.__piece.getTabWithIndex())))
        self.placePiece(Piece.col, Piece.row)

    def pivot(self):
        """ write docstrings """
        self.erasePiece()
        if self.canPlacePiece(Piece.col, Piece.row, self.__piece.getTab()[self.__piece.getNextNumTab()]): self.__piece.pivotPiece()
        self.placePiece(Piece.col, Piece.row)

    def downPiece(self):
        """ write docstrings """
        self.erasePiece()
        if self.canPlacePiece(Piece.col, Piece.row+1): self.__piece.goDown()
        self.placePiece(Piece.col, Piece.row)

    def autoControl(self, counter: int):
        """ write docstrings """
        if counter == 0: 
            self.erasePiece()
            if self.canPlacePiece(Piece.col, Piece.row+1):
                self.downPiece()
                self.__score+=1
            else:
                self.placePiece(Piece.col, Piece.row)
                self.updatePlatform()
                self.changePiece()

    def rowIsFull(self, index: int):
        """ write docstrings """
        assert(index in range(Display.HEIGHT_PLATFORM)), 'index not in range.'
        return 0 not in self.__platform[index]
    
    def breakRow(self, index: int):
        """ write docstrings """
        self.__platform[index] = [1 if i in (0, Display.WIDTH_PLATFORM-1) else 0 for i in range(Display.WIDTH_PLATFORM)]

    def goDownRow(self, row):
        """ write docstrings """
        empty_row = [1 if i in (0, Display.WIDTH_PLATFORM-1) else 0 for i in range(Display.WIDTH_PLATFORM)]
        if self.__platform[row] != empty_row and self.__platform[row+1] == empty_row:
            while row > 1 and self.__platform[row+1] == empty_row:
                self.__platform[row+1] = self.__platform[row].copy()
                self.__platform[row] = empty_row.copy()
                row -= 1

    def updatePlatform(self):
        """ write docstrings """
        for i in range(1, Display.HEIGHT_PLATFORM-1):
            if self.rowIsFull(i):
                self.breakRow(i)
                self.goDownRow(i-1)

    def placePieceInItsFinalPos(self):
        """ write docstrings """
        self.erasePiece()
        while(self.canPlacePiece(Piece.col, Piece.row+1)):
            Piece.row+=1
            self.__score += 1
        self.placePiece(Piece.col, Piece.row)

    def process_events_GUIs(self, e: pygame.event, isOver: bool=False, isPaused: bool=False):
        """ write docstrings """
        if isOver: 
            self.__OVER_GUI.manager.process_events(e)
        elif isPaused:
            self.__PAUSE_GUI.pause_manager.process_events(e)
            self.__PAUSE_GUI.manager.process_events(e)
        else:
            self.__MAIN_GUI.unpause_manager.process_events(e)
            self.__MAIN_GUI.manager.process_events(e)

    def update_GUIs(self, isOver: bool=False, isPaused: bool=False):

        db = DataBase()

        if isOver: 
            self.__OVER_GUI.scoreText.set_text("score: " + str(self.__score))
            self.__OVER_GUI.highScoreText.set_text("highScore: " + str(db.getHighScore()))
            self.__OVER_GUI.manager.update(Display.TIME_DELTA)
            self.__OVER_GUI.manager.draw_ui(self.__surface)
        elif isPaused: 
            self.__PAUSE_GUI.pause_manager.update(Display.TIME_DELTA)
            self.__PAUSE_GUI.pause_manager.draw_ui(self.__surface)
            self.__PAUSE_GUI.manager.draw_ui(self.__surface)
            self.__PAUSE_GUI.manager.update(Display.TIME_DELTA)
        else: 
            self.__MAIN_GUI.scoreText.set_text("score: " + str(self.__score))
            self.__MAIN_GUI.unpause_manager.update(Display.TIME_DELTA)
            self.__MAIN_GUI.manager.update(Display.TIME_DELTA)
            self.__MAIN_GUI.unpause_manager.draw_ui(self.__surface)
            self.__MAIN_GUI.manager.draw_ui(self.__surface)

    def getScore(self):
        return self.__score
        
    def getMain(self):
        return self.__MAIN_GUI

    def getPause(self):
        return self.__PAUSE_GUI

    def getOver(self):
        return self.__OVER_GUI
    