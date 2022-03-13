import pygame
import pygame_gui

class GUI_Infos:
    pygame.display.init()
    def __init__(self, longueur, largeur):    
        self.manager = pygame_gui.UIManager((longueur, largeur))
        self.pause_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((-60, 15),(50, 50)),
            text='PAUSE',
            manager=self.manager, anchors={'left': 'right', 'right':'right', 'top': 'top', "bottom": 'top'})


class GUI_Pause(GUI_Infos):
    """"""
    def __init__(self, longueur, largeur):
        super().__init__(longueur, largeur)
        self.pause_manager = pygame_gui.UIManager((longueur, largeur), 'json/UI_Label_Pause.json')
        self.resume_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((550,250), (400, 75)),
            text='RESUME', manager=self.pause_manager)

        self.quit_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((550,350), (400, 75)),
            text='QUIT', manager=self.pause_manager)

class GUI_UnPause(GUI_Infos):
    """"""
    def __init__(self, longueur, largeur,joueur):
        """"""
        super().__init__(longueur, largeur)
        self.unpause_manager = pygame_gui.UIManager((longueur, largeur), 'json/UI_Label_UnPause.json')
        self.scoreText = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((550,250), (200, 75)),
            manager=self.unpause_manager, text="score: " + str(joueur.score))
        self.highScoreText = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((550,350), (200, 75)),
            manager=self.unpause_manager, text="highScore: " + str(joueur.meilleurScore))

class GUI_GameOver():
    """"""
    def __init__(self, longueur, largeur, joueur):
        """"""
        self.manager = pygame_gui.UIManager((longueur, largeur), 'json/UI_Label_Pause.json')
        self.scoreText = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((550,150), (200, 75)),
            manager=self.manager, text="score: " + str(joueur.score))

        self.highScoreText = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((750,150), (200, 75)),
            manager=self.manager, text="highScore: " + str(joueur.meilleurScore))

        self.restart_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((550,250), (400, 75)),
            text='RESTART', manager=self.manager)

        self.quit_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((550,350), (400, 75)),
            text='QUIT', manager=self.manager)
