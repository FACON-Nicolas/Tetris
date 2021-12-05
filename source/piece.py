import pygame, sys
from pygame.locals import *
from Affichage import affichage
from Jeu import Jeu

Tetris = affichage()
Tetris.spawn_piece()
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
        elif event.key == KEYUP and event.key in Tetris.gameplay.Touches:
            Tetris.gameplay.Touches.remove(event.key)
        
    if not Tetris.gameplay.isDown:
        if K_UP in Tetris.gameplay.Touches:
            pass

    #mise à jour du jeu    
    Tetris.affichage_de_la_grille()
    #mise à jour de l'ecran
    pygame.display.flip()
#fin de la boucle -> fin du programme.
pygame.quit()
sys.exit()
