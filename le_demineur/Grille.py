#coding=utf-8

from random import randint
from Case import*

    
class Grille :

    
    def __init__(self, largeur, longueur, taille_case,origine,listImg,grille = None) :
        self.largeur = largeur
        self.longueur = longueur
        self.taille_case = taille_case
        self.grille = grille
        self.origine = origine   
        self.listImg = listImg
         
    def nouvelle_grille(self) :
        """
        Creer une nouvelle grille constituée de cases numérotés et de bombes
        """
        grille = []
        for j in range(self.largeur) :
            ligne = []
            for i in range(self.longueur) :
                case = Case(self.taille_case)
                if randint(1,7) == 1 :
                    case.pieger()
                ligne.append(case)
                
            grille.append(ligne)
        for y in range (len(grille)) :
            for x in range(len(grille[y])) :
                n_bombes = 0
                for i in range(-1,2) :
                    for j in range(-1,2) :
                        if 0 <= x+i < len(grille[y]) and 0 <= y+j < len(grille) :
                            if grille[y+j][x+i].get_piege() :
                                n_bombes += 1
                            
                grille[y][x].set_numero(n_bombes)
                grille[y][x].set_img1(self.listImg[n_bombes])
                grille[y][x].set_img2(self.listImg[9])
                grille[y][x].set_img3(self.listImg[11])
        self.grille = grille
        
    
    def afficher_grille(self) :
        """
        Affiche la grille à l'écran
        """
        
        
        y = self.taille_case/2
        x = 0
        origine_y = self.origine[0]
        origine_x = self.origine[1]
        for ligne in self.grille :
            origine_x = self.origine[1]
            x = self.taille_case/2
            for case in ligne :
                pushMatrix();
                translate(origine_x,origine_y);
                case.afficher_case(x,y)
                popMatrix();
                origine_x += self.taille_case
            origine_y += self.taille_case
  
    def get_largeur() : 
        return self.longueur
      
    def get_longeur() :
        return self.largeur
    
    def get_taille_case() :
        return self.taille_case
    
    def set_largeur(x) :
        self.largeur = x
        
    def set_longueur(x) :
        self.longueur = x
        
    def set_taille_case(x) :
        self.taille_case = x
