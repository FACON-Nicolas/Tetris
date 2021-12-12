import pygame, sys
from pygame.locals import *
import pygame_gui
from Affichage import affichage

Tetris = affichage()
Tetris.infos.highScoreText.set_text("highScore: " + str(Tetris.gameplay.meilleurScore))

#boucle du jeu
while Tetris.gameplay.game_running:
    #gestion du nombre de frames
    Tetris.CLOCK.tick(60)
    time_delta = 1
    #gestion des evenements
    for event in pygame.event.get():
        if event.type == QUIT:
            Tetris.gameplay.sauvegarder_les_donnees()
            Tetris.gameplay.game_running = False

        elif event.type == KEYDOWN and event.key not in Tetris.gameplay.Touches:
            Tetris.gameplay.Touches.append(event.key)

        elif event.type == KEYUP and event.key in Tetris.gameplay.Touches:
            Tetris.gameplay.Touches.remove(event.key)
            Tetris.gameplay.isDown = False

        elif event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == Tetris.infos.pause_button:
                    Tetris.gameplay.isGamePaused = not Tetris.gameplay.isGamePaused
                    if Tetris.gameplay.isGamePaused: pygame.mixer.music.pause()
                    else: pygame.mixer.music.unpause()
                elif event.ui_element in (Tetris.pause.quit_button, Tetris.end.quit_button):
                    Tetris.gameplay.game_running = False
                elif event.ui_element == Tetris.pause.resume_button:
                    Tetris.gameplay.isGamePaused = False
                elif event.ui_element == Tetris.end.restart_button:
                    Tetris.__init__()

        Tetris.infos.manager.process_events(event)
        Tetris.pause.pause_manager.process_events(event)
        Tetris.infos.unpause_manager.process_events(event)
        Tetris.end.manager.process_events(event)
    #si la touche echap est pressee
    if (K_ESCAPE in Tetris.gameplay.Touches) and not(Tetris.gameplay.isDown) and (Tetris.gameplay.isInGame):
        Tetris.gameplay.isDown = True
        Tetris.gameplay.isGamePaused = not Tetris.gameplay.isGamePaused
        if Tetris.gameplay.isGamePaused: pygame.mixer.music.pause()
        else: pygame.mixer.music.unpause()        

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
                    Tetris.gameplay.augmenterScore()
                Tetris.afficher_piece(Tetris.piece, Tetris.piece.get_tab_with_index())

        if not K_DOWN in Tetris.gameplay.Touches: Tetris.gameplay.vitesse = 60
        if Tetris.gameplay.isInGame:
            if Tetris.gameplay.compteur % Tetris.gameplay.vitesse == 0:
                if Tetris.piece.get_tab() != []:
                    Tetris.effacer_piece(Tetris.piece, Tetris.piece.get_tab_with_index())
                    if Tetris.peut_bouger_piece(Tetris.piece.x, Tetris.piece.y+1, Tetris.piece.get_tab_with_index()):
                        Tetris.piece.descendre()
                        Tetris.gameplay.augmenterScore()
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
                        print(Tetris.gameplay.score)
                        Tetris.gameplay.changerMeilleurScore()
                        Tetris.gameplay.sauvegarder_les_donnees()
                        Tetris.gameplay.isInGame = False
                else:
                    Tetris.choisir_piece()
                    Tetris.placer_piece()
                    Tetris.grille = Tetris.initialisation_de_la_grille()
                    Tetris.spawn_piece()
        Tetris.infos.unpause_manager.update(time_delta)
        Tetris.infos.unpause_manager.draw_ui(Tetris.surface)
        #Mise a jour du compteur permettant de contrôler la vitesse de déplacement d'une piece
        Tetris.gameplay.compteur += 1
        #mise à jour du jeu    
        Tetris.reparer_grille()
        Tetris.affichage_de_la_grille()
        Tetris.infos.scoreText.set_text("score: " + str(Tetris.gameplay.score))
        Tetris.infos.manager.update(time_delta)
        Tetris.infos.manager.draw_ui(Tetris.surface)
        Tetris.infos.unpause_manager.update(time_delta)
        Tetris.infos.unpause_manager.draw_ui(Tetris.surface)
    elif Tetris.gameplay.isGamePaused:
        Tetris.pause.pause_manager.update(time_delta)
        Tetris.pause.pause_manager.draw_ui(Tetris.surface)
        gamePaused = pygame.font.SysFont('Arial', 60, bold=True)
        text = gamePaused.render('GAME PAUSED',True, (255,255,255))
        Tetris.surface.blit(text, (525,50))
    if not Tetris.gameplay.isInGame:
        Tetris.end.scoreText.set_text("score: " + str(Tetris.gameplay.score))
        Tetris.end.highScoreText.set_text("highScore: " + str(Tetris.gameplay.meilleurScore))
        Tetris.end.manager.update(time_delta)
        Tetris.end.manager.draw_ui(Tetris.surface)
        gameOver = pygame.font.SysFont('Arial', 60, bold=True)
        textOver = gameOver.render('GAME OVER',True, (255,255,255))
        Tetris.surface.blit(textOver, (575,50))
    #mise à jour de l'ecran
    pygame.display.flip()
#fin de la boucle -> fin du programme.
pygame.quit()
sys.exit()
