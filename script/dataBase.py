from datetime import datetime
import os
import sqlite3

class DataBase: 

    path = os.path.expandvars(R'C:\Users\$USERNAME\Documents\Database-Tetris')
    file = os.path.expandvars(R'C:\Users\$USERNAME\Documents\Database-Tetris\Table.db')

    def __init__(self):
        """ TODO: Write docstrings """
        self.__connexion = None
        if not os.path.exists(DataBase.path): os.mkdir(DataBase.path)
        if not os.path.exists(DataBase.file):
            self.__connexion = sqlite3.connect(DataBase.file)
            self.__cursor = self.__connexion.cursor()
            self.__cursor.execute("""CREATE TABLE JOUEUR (
                                    nom VARCHAR NOT NULL, 
                                    score BIGINT NOT NULL,
                                    dateGame DATE)""")
        self.__connexion = sqlite3.connect(DataBase.file)
        self.__cursor = self.__connexion.cursor()

    def __del__(self):
        """ write docstrings """
        self.__connexion.commit()
        self.__connexion.close()

    def addGame(self, player: str, score: int, date: datetime=None):
        """ write docstrings """
        if date is None: date = datetime.now().date()
        query = "INSERT INTO JOUEUR VALUES (?, ?, ?)"
        self.__cursor.execute(query, (player, score, date))
        self.__connexion.commit()

    def deleteGame(self, player: str, score: int):
        """ write docstrings """
        query = """DELETE FROM JOUEUR 
                   WHERE nom=? AND score=?"""
        return self.__cursor.execute(query, (player, score,))

    def getBestGame(self):
        """ write docstrings """
        query = """SELECT * 
                   FROM JOUEUR 
                   ORDER BY SCORE DESC 
                   LIMIT 5"""

        return self.__cursor.execute(query)
    
    def getBestGameByPlayer(self, player: str):
        """ write docstrings """
        query = """SELECT * 
                   FROM JOUEUR 
                   WHERE nom = ? 
                   ORDER BY SCORE DESC 
                   LIMIT 5"""

        return self.__cursor.execute(query, (player))

    def getHighScore(self):
        """ write docstrings """
        return self.__cursor.execute("""SELECT MAX(score) 
                                        FROM JOUEUR""")

    def getBestPlayer(self):
        """ write docstrings """
        return self.__cursor.execute("""SELECT nom 
                                        FROM JOUEUR 
                                        WHERE score = (SELECT MAX(score) FROM JOUEUR)""")
                                            
    def executeQuery(self, query: str):
        """ write docstrings """
        return self.__cursor.execute(query)
