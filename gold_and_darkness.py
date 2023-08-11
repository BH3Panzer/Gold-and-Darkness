from math import *

import pygame as pg

pg.init()
fps = 60  # Les fps wesh
run = True
clock = pg.time.Clock()
WIDTH = 1000
HEIGHT = 800
screen = pg.display.set_mode((WIDTH, HEIGHT), pg.DOUBLEBUF)
pg.display.set_caption('Gold and Darkness')
pg.mixer.pre_init(buffer=512)
background = pg.Rect(0, 0, WIDTH, HEIGHT)
l = locals()  # C est le classic lui
camerax = 0  # Position x default camera
cameray = 0  # Position y default camera
hendek = pg.font.SysFont(None,50) #définie la police


# Class pour le jeu pour une partie
class Game:
    def __init__(self, player, map):
        self.player = player  # Objet joueur dans le jeu
        self.map = map  # Objet de la map


# Class pour le joueur
class Player:
    def __init__(self, x, y, pv):
        # Coordonnees joueur:
        self.x = x
        self.y = y
        self.pv = pv  # Vie joueur
        self.up = False
        self.down = False
        self.left = False
        self.right = False

    def draw(self):
        pg.draw.circle(screen, (255, 0, 0), (self.x-camerax, self.y-cameray), 5, 0, False, False, False, False)


# Class pour la map
class Map:
    def __init__(self, xsize, ysize):
        self.size = [xsize, ysize]  # Taille de la map
        self.size[0] = int(self.size[0])
        self.size[1] = int(self.size[1])

    def drawMap(self):
        total = self.size[0] * self.size[1]
        for i in range(int(total)):
            l["tile" + str(i)].draw()

    def generateMap(self):
        i = 0
        for x in range(int(self.size[0])):
            for y in range(int(self.size[1])):
                l["tile" + str(i)] = Tile(x * 15, y * 15, 2, wall=False)
                l["tile" + str(i)].loadTexture()
                i += 1


# Class pour toute entitee
# autre que le joueur
class Entity:
    def __init__(self, x, y):
        # Position entitee:
        self.x = x
        self.y = y


class Tile:
    def __init__(self, x, y, texture, wall=False):
        self.player_distance = 0
        self.wall = wall  # Si True est un mur sinon un chemin
        # Position tuile de depart (en haut a gauche):
        self.x = x
        self.y = y
        self.texture = texture # Numéro texture de la tuile
        self.image = None #Init image

    def loadTexture(self):  # Charge la texture de la tuile
        self.image = pg.image.load('tiles/tile'+str(self.texture)+'.png')
        self.image = self.image.convert_alpha()


    def changeLight(self):  # Règle la lumiere (dans la boucle obligatoire avant draw)
        self.dark = 150
        self.calculateDistance()
        if self.wall == True:
            self.dark -= 30
        if self.player_distance <=150:
            self.dark -= int(self.player_distance/1.5)
        else:
            self.dark = 0
        if self.dark < 0:
            self.dark = 0
        self.image.set_alpha(self.dark)

    def calculateDistance(self):
        self.player_distance = sqrt(abs((self.x + 7) - player.x) ** 2 + abs((self.y + 7) - player.y) ** 2)

    def draw(self):  # Dessine une tuile
        self.changeLight()
        screen.blit(self.image, (self.x-camerax, self.y-cameray))



player = Player(WIDTH/2, HEIGHT/2, 100) 



map = Map(WIDTH / 15, HEIGHT / 15)
map.generateMap()
while run:
    pg.draw.rect(screen, (0, 0, 0), background)
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                player.up = True
            if event.key == pg.K_DOWN:
                player.down = True
            if event.key == pg.K_LEFT:
                player.left = True
            if event.key == pg.K_RIGHT:
                player.right = True

        if event.type == pg.KEYUP:
            if event.key == pg.K_UP:
                player.up = False
            if event.key == pg.K_DOWN:
                player.down = False
            if event.key == pg.K_LEFT:
                player.left = False
            if event.key == pg.K_RIGHT:
                player.right = False
        if event.type == pg.QUIT:
            pg.quit()

    map.drawMap()
    if player.up:
        player.y -= 2
        cameray -= 2
    if player.down:
        player.y += 2
        cameray += 2
    if player.left:
        player.x -= 2
        camerax -= 2
    if player.right:
        player.x += 2
        camerax += 2
    player.draw()
    
    texte = hendek.render(str(int(clock.get_fps())),True,(255,255,255)) #prend les fps pour les afficher
    screen.blit(texte,(900,10)) #affiche les fps directement dans le jeu

    pg.display.flip()
    clock.tick(fps)
