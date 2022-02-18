import os, json

class Jeu:
    """ permet de reunir en une classe 
     des fonctionnalites du Tetris """
    def __init__(self):
        """ initialisation du jeu """
        self.game_running = True
        self.isDown = False
        self.isInGame = True
        self.isGamePaused = False
        self.Touches = list()
        self.compteur = 0
        self.vitesse = 60
        self.score = 0
        self.fichier = "json/save.json"
        self.donnees = self.ouvrirJson()
        self.meilleurScore = 0
        self.chargerDonnees()

    def augmenterScore(self):
        """ permet d'augmenter le score du joueur """
        self.score += 1

    def changerMeilleurScore(self):
        """ permet de changer le meilleur score
        si jamais le joueur bat ce dernier """
        if self.score > self.meilleurScore:
            self.meilleurScore = self.score
            self.sauvegarder_les_donnees()

    def chargerDonnees(self):
        """ permet de charger le meilleurScore """
        if not self.donnees == {}:
            self.meilleurScore = self.donnees['highScore']

    def ouvrirJson(self):
        """ permet de charger un fichier stocké en json """
        if os.path.exists(self.fichier):
            with open(self.fichier) as open_json:
                return json.load(open_json)
        else:
            return {'highScore': 0}

    def sauvegarder_les_donnees(self):
        """ permet de sauvegarder les donnees d'un utilisateur """
        self.donnees['highScore'] = self.meilleurScore
        with open(self.fichier, 'w') as f:    
            j = json.dump(self.donnees, f)