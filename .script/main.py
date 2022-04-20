import os
import pygame
import pygame_gui
from pygame.locals import *
from Display import Display
from Color import Color
from dataBase import DataBase
from piece import Piece
from audio import Sound


class Main:

    keys = list()
    isPaused=False
    isOver=False
    keyIsDown=False
    database = DataBase()

    def __init__(self):
        self.__isRunning = True
        self.__screen = Display()
        self.__clock = pygame.time.Clock()
        self.__counter = 0
        self.__speed = 45
        self.__mixer = Sound()

    @staticmethod
    def isKeyDown():
        Main.keyIsDown = len(Main.keys) > 0

    def run(self): 
        """ write docstrings """
        self.__screen.spawnPiece()
        while self.__isRunning:
            self.setSpeed()
            self.event()
            self.controls()
            self.controlsPaused()
            self.controlsGameOver()
            if not Main.isOver and not Main.isPaused: self.__screen.autoControl(self.__counter)
            if not Main.isPaused:
                self.__screen.showPlatform()
                self.isGameOver()
            self.__screen.update_GUIs(Main.isOver, Main.isPaused)
            Main.isKeyDown()
            pygame.display.flip()


    def event(self):
        """ write docstrings """
        self.__clock.tick(60)
        if not Main.isOver and not Main.isPaused: self.__counter = (self.__counter + 1) % self.__speed
        for event in pygame.event.get():
            if event.type == QUIT: self.__isRunning=False
            elif event.type == KEYDOWN and event.key not in Main.keys: Main.keys.append(event.key)
            elif event.type == KEYUP and event.key in Main.keys: Main.keys.remove(event.key)
            elif event.type == USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED: 
                    self.button_pressed(event)
            #elif event.type == VIDEOEXPOSE: self.__screen.setFullScreen()
            #elif event.type is VIDEORESIZE: self.__screen.resizeGame(event.w)
            self.__screen.process_events_GUIs(event, Main.isOver, Main.isPaused)

    def controls(self): 
        """ write docstrings """
        if (not Main.isOver and not Main.keyIsDown and not Main.isPaused):
            if Main.keys == [K_ESCAPE]: Main.isPaused = not Main.isPaused; Main.keys = []; pygame.mixer.music.pause()         
            elif Main.keys == [K_RIGHT]: self.__screen.moveRight()
            elif Main.keys == [K_LEFT]: self.__screen.moveLeft() 
            elif Main.keys == [K_UP]: self.__screen.pivot()    
            elif Main.keys == [K_SPACE]: 
                self.__counter = 0
                self.__screen.placePieceInItsFinalPos()

    def controlsPaused(self): 
        """ write docstrings """
        if (Main.isPaused and not Main.keyIsDown):
            if Main.keys == [K_ESCAPE]:
                Main.isPaused = not Main.isPaused
                pygame.mixer.music.unpause()
                 
    def controlsGameOver(self):
        """ write docstrings """
        if (Main.isOver and not Main.keyIsDown): 
            if Main.keys == [K_SPACE]: pass

    def setSpeed(self):
        """ write docstrings """
        if Main.keys == [K_DOWN]: self.__speed = 3
        else: 
            score = 30 if self.__screen.getScore() > 9000 else self.__screen.getScore() // 300
            self.__speed = 45 - score

    def augmenterScore(self):
        """ write docstrings """
        self.__score += 1

    def isGameOver(self):
        """ write docstrings """
        self.__screen.erasePiece()
        over = Main.isOver
        Main.isOver = ((Piece.col, Piece.row) == (Display.WIDTH_PLATFORM//2, 0) and \
             not self.__screen.canPlacePiece(Piece.col, Piece.row))
        if (not over and Main.isOver) :
            Main.database.addGame(os.environ.get('USERNAME'), self.__screen.getScore())
        self.__screen.placePiece(Piece.col, Piece.row)

    def button_pressed(self, e: pygame.event):
        if e.ui_element in (self.__screen.getMain().pause_button, self.__screen.getPause().pause_button, self.__screen.getPause().resume_button): #pause_button is main pause button and paused pause button
            if not Main.isPaused : 
                pygame.mixer.music.pause()
                Main.isPaused = True
            else: 
                pygame.mixer.music.unpause()
                Main.isPaused = False
        elif e.ui_element in (self.__screen.getPause().quit_button, self.__screen.getOver().quit_button):
            self.__isRunning = False
        elif e.ui_element == self.__screen.getOver().restart_button: self.__init__()

m=Main()
m.run()