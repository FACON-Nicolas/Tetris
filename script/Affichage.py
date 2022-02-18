import pygame
from GUI import *
from random import randint
from piece import Piece
from Jeu import Jeu
from math import sqrt
from audio import sound

class affichage:
    """ permet de gerer les différents cas d'affichage des programmes """

    def __init__(self):
        """ initialisation de la classe 'Affichage' """
        pygame.init()
        self.gameplay = Jeu()
        #initialisation des constantes
        self.MIN_GRILLE = 0
        self.MAX_GRILLE_H = 22
        self.MAX_GRILLE_L = 12
        self.LONGUEUR_FENETRE = 1174
        self.LARGEUR_FENETRE = 660
        self.CLOCK = pygame.time.Clock()
        #initialisation de la grille
        self.grille = self.initialisation_de_la_grille()        
        #initialisation des tableau des pieces du jeu
        self.I = [[0,2,0,0,2,0,0,2,0],[0,0,0,2,2,2,0,0,0],[0,2,0,0,2,0,0,2,0],[0,0,0,2,2,2,0,0,0]]
        self.T = [[0,0,0,4,4,4,0,4,0],[0,4,0,0,4,4,0,4,0],[0,4,0,4,4,4,0,0,0],[0,4,0,4,4,0,0,4,0]]
        self.J = [[0,0,0,5,5,5,0,0,5],[0,5,0,0,5,0,5,5,0],[5,0,0,5,5,5,0,0,0],[0,5,5,0,5,0,0,5,0]]
        self.L = [[0,0,0,6,6,6,6,0,0],[0,6,0,0,6,0,0,6,6],[0,0,6,6,6,6,0,0,0],[6,6,0,0,6,0,0,6,0]]
        self.Z = [[0,0,0,8,8,0,0,8,8],[0,8,0,8,8,0,8,0,0],[0,0,0,8,8,0,0,8,8],[0,8,0,8,8,0,8,0,0]]
        self.S = [[0,0,0,0,7,7,7,7,0],[7,0,0,7,7,0,0,7,0],[0,0,0,0,7,7,7,7,0],[7,0,0,7,7,0,0,7,0]]
        self.O = [[3,3,0,3,3,0,0,0,0],[3,3,0,3,3,0,0,0,0],[3,3,0,3,3,0,0,0,0],[3,3,0,3,3,0,0,0,0]]
        #initialisation des pieces du jeu
        self.P_I = Piece(self.I)
        self.P_T = Piece(self.T)
        self.P_L = Piece(self.L)
        self.P_J = Piece(self.J)
        self.P_Z = Piece(self.Z)
        self.P_S = Piece(self.S)
        self.P_O = Piece(self.O)
        #initialisation du visuel
        self.surface = pygame.display.set_mode((self.LONGUEUR_FENETRE, self.LARGEUR_FENETRE))
        self.nom_fenetre = pygame.display.set_caption('Tetris')
        self.gris = pygame.image.load('cases/grey.png').convert_alpha()
        self.rouge = pygame.image.load('cases/red.png').convert_alpha()
        self.vert = pygame.image.load('cases/green.png').convert_alpha()
        self.noir = pygame.image.load('cases/black.png').convert_alpha()
        self.jaune = pygame.image.load('cases/yellow.png').convert_alpha()
        self.orange = pygame.image.load('cases/orange.png').convert_alpha()
        self.violet = pygame.image.load('cases/purple.png').convert_alpha()
        self.bleu_clair = pygame.image.load('cases/sky_blue.png').convert_alpha()
        self.bleu_fonce = pygame.image.load('cases/dark_blue.png').convert_alpha()
        self.liste_couleurs = self.liste_des_couleurs()
        #gameplay
        self.piece = Piece([])
        self.son = sound()
        #GUIs
        self.infos = GUI_UnPause(self.LONGUEUR_FENETRE, self.LARGEUR_FENETRE, self.gameplay)
        self.pause = GUI_Pause(self.LONGUEUR_FENETRE, self.LARGEUR_FENETRE)
        self.end = GUI_GameOver(self.LONGUEUR_FENETRE, self.LARGEUR_FENETRE, self.gameplay)

    def initialisation_de_la_grille(self):
        """ permet l'initialisation de la grille
        :return: grille du jeu initialisee
        :rtype: List[List[int]] """
        return [[1 if i in (self.MIN_GRILLE, self.MAX_GRILLE_L-1)  or j in (self.MIN_GRILLE, self.MAX_GRILLE_H - 1) \
            else 0 for i in range(self.MAX_GRILLE_L)] for j in range(self.MAX_GRILLE_H)]

    def reparer_grille(self):
        for l in range(len(self.grille)):
            for c in range(len(self.grille[0])):
                if l in (self.MIN_GRILLE, self.MAX_GRILLE_H-1) or c in(self.MIN_GRILLE, self.MAX_GRILLE_L-1):
                    self.grille[l][c] = 1

    def liste_des_couleurs(self):
        """ permet de lister les couleurs des pieces, l'index reference 
        aussi la couleur de chacune des pieces dans la grille du jeu. 
        :return: liste des couleurs
        :rtype: List[List[List[int]]] """
        return [self.noir, self.gris, self.bleu_clair, self.jaune, self.violet, self.orange, self.bleu_fonce, self.rouge, self.vert]

    def liste_des_pieces(self):
        """ permet de listes l'ensemble des pieces du jeu Tetris
        :return : listes des pieces
        :rtype : List[List[List[int]]] """
        return [self.P_I, self.P_J, self.P_L, self.P_O, self.P_S, self.P_T, self.P_Z]

    def choisir_piece(self):
        """ permet de choisir une piece aléatoirement dans la liste """
        index_piece = randint(0, len(self.liste_des_pieces())-1)
        liste_piece = self.liste_des_pieces()

        if self.piece != []:
            while liste_piece[index_piece] == self.piece:
                index_piece = randint(0, len(self.liste_des_pieces())-1)
            self.piece = liste_piece[index_piece]

    def affichage_de_la_grille(self):
        """ permet d'afficher la grille """
        couleur = (50,50,50)
        self.surface.fill(couleur)
        for c in range(len(self.grille[0])):
            for l in range(len(self.grille)):
                couleur = self.grille[l][c]
                carre = self.liste_couleurs[couleur].copy()
                self.surface.blit(carre, (c*30, l*30))

    def effacer_piece(self, piece, tableau):
        """ permet de 'nettoyer' la surface sur laquelle une pièce 
        a été avant de potentiellement la bouger vers un autre endroit (ou la pivoter). 
        :param piece : matrice de la pièce qu'on souhaite effacer
        :type piece : Piece """
        for i in range(len(tableau)):
            if tableau[i] != 0:
                horizontal, vertical = (i % int(sqrt(len(tableau))) + piece.x), (i // int(sqrt(len(tableau))) + piece.y)
                self.grille[vertical][horizontal] = 0

    def afficher_piece(self, piece, tableau):
        """ permet d'afficher la pièce à un endroit de la surface 
        après qu'elle ait potientiellement été nettoyé juste avant. 
        :param piece : matrice de la pièce qu'on souhaite afficher
        :type piece : Piece """
        for i in range(len(tableau)):
            if tableau[i] != 0:
                horizontal, vertical = (i % int(sqrt(len(tableau))) + piece.x), ((i // int(sqrt(len(tableau)))) + piece.y)
                self.grille[vertical][horizontal] = tableau[i]

    def peut_bouger_piece(self, x: int, y: int, tableau: list):
        """ renvoie vrai ou faux en fonction de la capacité
        d'afficher la piece en argument dans la grille de jeu 
        :param x : index horizontal de la piece 
        :param y : index vertical de la piece
        :param piece : matrice de la piece qu'on souhaite bouger
        :type x : int
        :type y : int
        :type piece : Piece
        """
        for i in range(len(tableau)):
            if tableau[i] != 0:
                horizontal, vertical = (i % int(sqrt(len(tableau))) + x), (i // int(sqrt(len(tableau))) + y)
                if self.grille[vertical][horizontal] != 0: 
                    if self.grille[vertical][horizontal] == 1:
                            return False
                    else: return False
        return True

    def spawn_piece(self):
        """ permet de faire spawn une nouvelle pièce lorsque la derniere est place 
        :todo :: permettre de changer l'axe des abscisses si jamais la valeur par
        defaut n'est pas disponible pour le placement de la piece du Tetris. """
        if self.piece.x != -1:
            tab = self.piece.tableau[self.piece.num_tableau]
            self.afficher_piece(self.piece, tab)

    def ligne_pleine(self, nombre):
        """ permet de savoir si une ligne est pleine ou non
        :args : None 
        :return : ligne pleine ou non
        :rtype : bool """
        return not 0 in self.grille[nombre]

    def destruction_de_la_ligne(self, nombre):
        """ permet de détruire / initialiser les lignes de la grille de jeu """
        self.grille[nombre] = [1 if i in (self.MIN_GRILLE, self.MAX_GRILLE_L-1) else 0 for i in range(len(self.grille[nombre]))]

    def recuperer_la_ligne_du_dessus(self, nombre):
        """ permet de faire descendre la grille lorsqu'une ligne de cette 
        derniere aura été détruite car elle aura été pleine d'autres cases """
        self.grille[nombre] = self.grille[nombre-1].copy()

    def placer_piece(self):
        """ permet de faire spawn une piece sur un axe horizontal
        particulier en fonction de remplissage de la grille du jeu """
        self.piece.initialiser_position()
        for i in range(0,len(self.grille[0])-3):
            if self.peut_bouger_piece(i,1,self.piece.get_tab_with_index()):
                self.piece.x = i
                break