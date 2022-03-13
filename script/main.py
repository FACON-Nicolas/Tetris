import os
import pygame
from pygame.locals import *
from Display import Display
from Color import Color
from dataBase import DataBase


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
        self.__score = 0

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
            self.__screen.autoControl(self.__counter)
            self.__screen.showPlatform()
            Main.isKeyDown()

    def event(self):
        """ write docstrings """
        self.__clock.tick(60)
        print('s: ', self.__speed)
        self.__counter = (self.__counter + 1) % self.__speed
        for event in pygame.event.get():
            if event.type == QUIT: self.__isRunning = False
            elif event.type == KEYDOWN and event.key not in Main.keys: Main.keys.append(event.key)
            elif event.type == KEYUP and event.key in Main.keys: Main.keys.remove(event.key)
            elif event.type == VIDEOEXPOSE: self.__screen.setFullScreen()
            elif event.type == VIDEORESIZE: self.__screen.resizeGame(event.w)

    def controls(self): 
        """ write docstrings """
        if (not Main.keyIsDown and not Main.isPaused):
            if Main.keys == [K_SPACE]: self.__screen.downPiece()
            elif Main.keys == [K_RIGHT]: self.__screen.moveRight()
            elif Main.keys == [K_LEFT]: self.__screen.moveLeft() 
            elif Main.keys == [K_UP]: self.__screen.pivot()    
            elif Main.keys == [K_ESCAPE]: pass      # set the game paused

    def controlsPaused(self): 
        """ write docstrings """
        if (Main.isPaused and not Main.keyIsDown):
            if Main.keys == [K_ESCAPE]: pass        #to set the game paused if the game is paused

    def controlsGameOver(self):
        """ write docstrings """
        if (Main.isOver and not Main.keyIsDown): 
            if Main.keys == [K_SPACE]: pass         #to play again

    def setSpeed(self):
        if Main.keys == [K_DOWN]: self.__speed = 3
        else: 
            score = 30 if self.__score > 30000 else self.__score // 1000
            self.__speed = 45 - score

m=Main()
m.run()