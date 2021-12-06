import pygame, sys
from pygame.locals import *
from Affichage import affichage
from Jeu import Jeu

Tetris = affichage()

#boucle du jeu
while Tetris.gameplay.game_running:
    #gestion du nombre de frames
    Tetris.CLOCK.tick(60)
    #gestion des evenements
    for event in pygame.event.get():
        if event.type == QUIT:
            Tetris.gameplay.game_running = False
        elif event.type == KEYDOWN and event.key not in Tetris.gameplay.Touches:
            Tetris.gameplay.Touches.append(event.key)
        elif event.type == KEYUP and event.key in Tetris.gameplay.Touches:
            Tetris.gameplay.Touches.remove(event.key)
            Tetris.gameplay.isDown = False

    #si la touche echap est pressee
    if K_ESCAPE in Tetris.gameplay.Touches and not Tetris.gameplay.isDown:
        Tetris.gameplay.isDown = True
        Tetris.gameplay.isGamePaused = not Tetris.gameplay.isGamePaused

    if not Tetris.gameplay.isGamePaused:
        #si aucune touche n'est pressee     
        if not Tetris.gameplay.isDown:
            #si la flèche du haut est pressee
            if K_UP in Tetris.gameplay.Touches:
                Tetris.effacer_piece(Tetris.piece, Tetris.piece.get_tab_with_index())
                if Tetris.peut_bouger_piece(Tetris.piece.x, Tetris.piece.y, Tetris.piece.get_tab()[(Tetris.piece.num_tableau+1)%4]):
                    Tetris.piece.pivoter_piece()
                Tetris.afficher_piece(Tetris.piece, Tetris.piece.get_tab_with_index())
                Tetris.gameplay.isDown = True

            #si la fleche de gauche est pressee
            elif K_LEFT in Tetris.gameplay.Touches:
                Tetris.effacer_piece(Tetris.piece, Tetris.piece.get_tab_with_index())
                if Tetris.peut_bouger_piece(Tetris.piece.x-1, Tetris.piece.y, Tetris.piece.get_tab_with_index()):
                    Tetris.piece.gauche()
                    Tetris.gameplay.isDown = True
                Tetris.afficher_piece(Tetris.piece, Tetris.piece.get_tab_with_index())
            
            #si la fleche de droite est pressee
            elif K_RIGHT in Tetris.gameplay.Touches:
                Tetris.effacer_piece(Tetris.piece, Tetris.piece.get_tab_with_index())
                if Tetris.peut_bouger_piece(Tetris.piece.x+1, Tetris.piece.y, Tetris.piece.get_tab_with_index()):
                    Tetris.piece.droite()
                    Tetris.gameplay.isDown = True
                Tetris.afficher_piece(Tetris.piece, Tetris.piece.get_tab_with_index())
            #si la fleche du bas est pressee
            elif K_DOWN in Tetris.gameplay.Touches: 
                Tetris.gameplay.vitesse = 3
            #si la touche espace est pressee
            elif K_SPACE in Tetris.gameplay.Touches: 
                Tetris.gameplay.isDown = True
                Tetris.effacer_piece(Tetris.piece, Tetris.piece.get_tab_with_index())
                while (Tetris.peut_bouger_piece(Tetris.piece.x, Tetris.piece.y + 1, Tetris.piece.get_tab_with_index())):
                    Tetris.piece.descendre()
                Tetris.afficher_piece(Tetris.piece, Tetris.piece.get_tab_with_index())

        if not K_DOWN in Tetris.gameplay.Touches: Tetris.gameplay.vitesse = 60
        if Tetris.gameplay.isInGame:
            if Tetris.gameplay.compteur % Tetris.gameplay.vitesse == 0:
                if Tetris.piece.get_tab() != []:
                    Tetris.effacer_piece(Tetris.piece, Tetris.piece.get_tab_with_index())
                    if Tetris.peut_bouger_piece(Tetris.piece.x, Tetris.piece.y+1, Tetris.piece.get_tab_with_index()):
                        Tetris.piece.descendre()
                        Tetris.afficher_piece(Tetris.piece, Tetris.piece.get_tab_with_index())
                    else: 
                        Tetris.afficher_piece(Tetris.piece, Tetris.piece.get_tab_with_index())
                        for i in range(2, len(Tetris.grille)-1):
                            if Tetris.ligne_pleine(i):
                                for j in range(i, 2, -1):
                                    Tetris.destruction_de_la_ligne(j)
                                    Tetris.recuperer_la_ligne_du_dessus(j)
                        Tetris.choisir_piece()
                        Tetris.placer_piece()
                    if Tetris.piece.x != -1:  
                        Tetris.spawn_piece()
                    else: 
                        Tetris.gameplay.isInGame = False
                else:
                    Tetris.choisir_piece()
                    Tetris.placer_piece()
                    Tetris.grille = Tetris.initialisation_de_la_grille()
                    Tetris.spawn_piece()
        #Mise a jour du compteur permettant de contrôler la vitesse de déplacement d'une piece
        Tetris.gameplay.compteur += 1
        #mise à jour du jeu    

        Tetris.reparer_grille()
        Tetris.affichage_de_la_grille()
    #mise à jour de l'ecran
    pygame.display.flip()
#fin de la boucle -> fin du programme.
pygame.quit()
sys.exit()
