from math import *
from kandinsky import *
from time import *
camerax=0 #Position x default camera
cameray=0 #Position y default camera
#Class pour le jeu pour une partie
class Game:
  def __init__(self,player,map):
    self.player=player #Objet joueur dans le jeu
    self.map=map #Objet de la map
    
#Class pour le joueur
class Player:
  def __init__(self,x,y,pv):
    #Coordonnees joueur:
    self.x=x
    self.y=y
    self.pv=pv #Vie joueur
    
#Class pour la map
class Map:
  def __init__(self,size):
    self.size=size #Taille de la map
    
#Class pour toute entitee 
#autre que le joueur
class Entity:
  def __init__(self,x,y):
    #Position entitee:
    self.x=x
    self.y=y
    
class Tile:
  def __init__(self,x,y,texture):
    #Position tuile de depart
    #(en haut a gauche):
    self.x=x
    self.y=y
    self.texture=texture #Texture d une tuile