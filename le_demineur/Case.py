#coding=utf-8
#
#        Module Case pour Le Démineur
#         
#           par Julien Goetghebeur
#                NSI 2021

class Case:
    def __init__(self, cote, img1=None, img2=None, img3 = None, devoile = False, marque = False, numero = 0, piege = False):
        self.cote = cote
        self.devoile = devoile
        self.marque = marque
        self.numero = numero
        self.piege = piege
        self.img1 = img1
        self.img2 = img2
        self.img3 = img3
    
    def get_cote(self):
        """
        Renvoie le côté de la case.
        """
        return self.cote
    def get_devoile(self):
        """
        Renvoie la valeur de devoile.
        """
        return self.devoile
    def get_marque(self):
        """
        Renvoie la valeur de marque.
        """
        return self.marque
    def get_numero(self):
        """
        Renvoie la valeur de numero.
        """
        return self.numero
    def get_piege(self):
        """
        Renvoie la valeur de piege.
        """
        return self.piege
    def set_cote(self, x):
        """
        La variable cote prend la valeur x.
        """
        self.cote = x
    def devoiler(self):
        """
        La variable devoile devient True.
        """
        self.devoile = True
    def marquer(self):
        """
        La variable marque devient True.
        """
        self.marque = True
    def demarquer(self):
        """
        La variable marque devient False.
        """
        self.marque = False
    def set_numero(self, x):
        """
        La variable numero prend la valeur x.
        """
        self.numero = x
    def pieger(self):
        """
        La variable piege devient True.
        """
        self.piege = True
    def set_img1(self, img):
        """
        La variable img1 devient img.
        """
        self.img1 = img
    def set_img2(self, img):
        """
        La variable img2 devient img.
        """
        self.img2 = img
    def set_img3(self, img):
        """
        La variable img3 devient img.
        """
        self.img3 = img
    def afficher_case(self, x, y):
        """
        Affiche l'image correspondant à l'état de la case:
            - img1 si la case est dévoilée
            - img3 si la case est marquée
            - img2 sinon
        """
        if self.devoile:
            image(self.img1,x,y,self.cote,self.cote)
        elif self.marque:
            image(self.img3,x,y,self.cote,self.cote)
        else:
            image(self.img2,x,y,self.cote,self.cote)
            
            
    
