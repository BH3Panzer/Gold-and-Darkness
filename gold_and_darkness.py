from math import *
from kandinsky import *
from time import *
from ion import *
l=locals() #C est le classic lui
camerax=0 #Position x default camera
cameray=0 #Position y default camera
tile_i={0:1,1:5,2:10} #Index pour texture tuile
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
  def draw(self):
    fill_circle(self.x,self.y,3,"r")
  
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
  def __init__(self,x,y,texture,wall=False):
    self.player_distance=0
    self.wall=wall #Si True est un mur sinon un chemin
    #Position tuile de depart
    #(en haut a gauche):
    self.x=x
    self.y=y
    self.texture=tile_i[texture] #Texture d une tuile
  def loadTexture(self): #Charge la texture de la tuile
    self.rectnum=0
    self.rects=[]
    file=open("tiles.py","r")
    for i in range(self.texture):
      file.readline()
    amount=file.readline()
    amount=int(amount)
    for i in range(amount):
      rect=file.readline()
      rect=rect.replace("\n","")
      rect=rect.split(",")
      self.rectnum+=1
      self.rects.append(rect)
  def changeLight(self): #Regle la lumiere (dans la boucle obligatoir avant draw)
    self.dark=0
    self.calculateDistance()
    if self.wall==True:
      self.dark+=75
    if self.player_distance>=10:
      self.dark+=20
    if self.player_distance>=25:
      self.dark+=40
    if self.player_distance>=50:
      self.dark+=60
  def calculateDistance(self):
    self.player_distance=sqrt(abs((self.x+7)-player.x)**2+abs((self.y+7)-player.y)**2)
  def draw(self): #Dessine une tuile
    self.changeLight()
    for i in range(self.rectnum):
      fill_rect(int(self.rects[i][0])+self.x,int(self.rects[i][1])+self.y,int(self.rects[i][2]),int(self.rects[i][3]),(int(self.rects[i][4])-self.dark,int(self.rects[i][5])-self.dark,int(self.rects[i][6])-self.dark))
player=Player(50,50,100)
def fill_c():
  i=0
  for x in range(6):
    for y in range(6):
      l["tile"+str(i)]=Tile(x*15,y*15,2,wall=False)
      l["tile"+str(i)].loadTexture()
      i+=1

def fill_d():
  for i in range(36):
    l["tile"+str(i)].draw()
fill_c()
while True:
  fill_rect(0,0,320,225,"black")
  if keydown(KEY_RIGHT):
    player.x+=5
  if keydown(KEY_DOWN):
    player.y+=5
  if keydown(KEY_LEFT):
    player.x-=5
  if keydown(KEY_UP):
    player.y-=5
  fill_d()
  player.draw()
  sleep(0.5)
