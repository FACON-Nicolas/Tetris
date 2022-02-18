class Piece:
    """ Classe utilisee pour initialiser la pièce d'un jeu Tetris """
    def __init__(self, tableau):
        """ initialisation de la classe piece
        :param tableau :: piece de jeu affichee dans une matrice
        :type tableau :: List[List[int]]

        :warnings :: le tableau doit avoir une taille de 3x3 """
        self.x = 0
        self.y = 0
        self.num_tableau = 0
        self.tableau = tableau

    def initialiser_position(self):
        self.x, self.y = -1, 0
        self.num_tableau = 0

    def descendre(self):
        """ procedure permettant de faire descendre 
        la pièce du jeu actuellement en mouvement. 
        :todo :: voir pour faire descendre le tableau """
        self.y +=1

    def gauche(self):
        """ Procedure permettant à la piece en question d'aller
        a gauche si elle remplit la condition de la fonction """
        self.x = self.x - 1 if self.x > 0 else self.x
    
    def droite(self):
        """ Procedure permettant à la piece en question d'aller
        a droite si elle remplit la condition de la fonction """
        self.x = self.x + 1 if self.x + 3 < 12 else self.x

    def pivoter_piece(self):
        """ permet de passer au tableau suivant d'une piece permettant 
        à la classe 'Affichage' de simuler un pivotement de la piece"""
        self.num_tableau = (self.num_tableau + 1) % 4

    def get_num_tab(self):
        return self.num_tableau

    def get_tab(self):
        return self.tableau

    def get_tab_with_index(self):
        return self.get_tab()[self.get_num_tab()]