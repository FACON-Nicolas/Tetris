import os
import sqlite3

class DataBase: 

    path = os.path.expandvars(R'C:\Users\$USERNAME\Documents\Database-Tetris')
    file = os.path.expandvars(R'C:\Users\$USERNAME\Documents\Database-Tetris\Table.db')

    def __init__(self):
        if not os.path.exists(DataBase.path): os.mkdir(DataBase.path)
        if not os.path.exists(DataBase.file): 
            connexion = sqlite3.connect(DataBase.file)
            cursor = connexion.cursor()
            cursor.execute('CREATE TABLE JOUEUR (nom VARCHAR NOT NULL, score BIGINT NOT NULL)')
        connexion = sqlite3.connect(DataBase.file)
            