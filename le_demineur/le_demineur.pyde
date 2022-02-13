#
#                  Le démineur 
#
#     par Julien Goetghebeur, Guyomarch Evan, Alex Roho
#                    NSI 2021
#

from Case import *
from ecran import *
from Grille import*


actuel = "accueil"
chrono = 0
resultat = "perdu"
taille_grille = (0,0)
choix = ''
clic = "non"
taille_case = 50
origineX = 0
origineY = 0

def setup():
    global img_fond, img_gagne, img_perdu, img_bouton_pause, imgCase, imgCaseBombe, imgCaseDrapeau, imgCase0, imgCase1, imgCase2, imgCase3, imgCase4, imgCase5,imgCase6, imgCase7, imgCase8, listImg,img_jeu
    size(1200,600)
    f = createFont("polices/Army.ttf",24)
    textFont(f)
    
    rectMode(CENTER)
    textAlign(CENTER)
    imageMode(CENTER)

    img_fond= loadImage("images/fond_demineur.jpg")
    img_jeu = loadImage("images/fond_jeu.png")
    img_gagne = loadImage("images/image_gagner.jpg")
    img_perdu = loadImage("images/image_perdu.jpg")
    img_bouton_pause = loadImage("images/pause.png")
    imgCase = loadImage("images/case_cache.png")
    imgCaseBombe = loadImage("images/case_bombe.png")
    imgCaseDrapeau = loadImage("images/case_drapeau.png")
    imgCase0 = loadImage("images/case_0.png")
    imgCase1 = loadImage("images/case_1.png")
    imgCase2 = loadImage("images/case_2.png")
    imgCase3 = loadImage("images/case_3.png")
    imgCase4 = loadImage("images/case_4.png")
    imgCase5 = loadImage("images/case_5.png")
    imgCase6 = loadImage("images/case_6.png")
    imgCase7 = loadImage("images/case_7.png")
    imgCase8 = loadImage("images/case_8.png")
    listImg = [imgCase0,imgCase1,imgCase2,imgCase3,imgCase4,imgCase5,imgCase6,imgCase7,imgCase8,imgCase,imgCaseBombe,imgCaseDrapeau]
    
    
def draw():
    global actuel,taille_grille,taille_case,resultat,grille,clic,chrono, chrono_debut,chrono_pause,chrono_pause_debut,chrono_pause_fin
    if actuel == "accueil":
        choix = ecran_accueil(img_fond,clic)
        if choix == "jouer":
            clic = "non"
            actuel = "difficulté"
        elif choix == "quitter":
            exit()
            
    elif actuel == "difficulté":
        choix = ecran_difficulte(img_fond,clic)
        if choix == "débutant":
            clic = "non"
            actuel = "jeu"
            taille_case = 50
            taille_grille = (9,9)
            initialisation()
        elif choix == "intermédiaire":
            clic = "non"
            actuel = "jeu"
            taille_grille = (16,16)
            taille_case = 30
            initialisation()
        elif choix == "difficile":
            clic = "non"
            actuel = "jeu"
            taille_grille = (32,16)
            taille_case = 30
            initialisation()
            
    elif actuel == "jeu":
        chrono = ((millis()-chrono_pause)-chrono_debut)/1000
        choix = ecran_jeu(img_jeu,img_bouton_pause,chrono,clic)
        if choix == "pause":
            clic = "non"
            actuel = "pause"
            chrono_pause_debut = millis()
        if partie_terminee(grille):
            chrono_fin = millis()
            resultat = "gagné"
            actuel = "fin"
        else:
            jeu()
            
    elif actuel == "pause":
        choix = ecran_pause(clic)
        if choix == "reprendre":
            clic = "non"
            actuel = "jeu"
            chrono_pause_fin = millis()-chrono_pause_debut
            chrono_pause += chrono_pause_fin
        elif choix == "recommencer":
            clic = "non"
            actuel = "jeu"
            initialisation()
        elif choix == "quitter":
            clic = "non"
            actuel = "accueil"
    
    elif actuel == "fin":
        choix = ecran_fin(img_gagne,resultat,chrono,img_perdu,clic)
        if choix == "rejouer":
            clic = "non"
            actuel = "jeu"
            initialisation()
        elif choix == "quitter":
            clic = "non"
            actuel = "accueil"

def jeu():
    global resultat, actuel, grille,clic
    grille.afficher_grille()
    if clic=="oui" and origineX <= mouseX <= width-origineX and origineY <= mouseY <= height-origineY and (mouseButton == LEFT):
        clic="non"
        x,y = entree_joueur()
        if not grille.grille[y][x].get_marque():
            if grille.grille[y][x].get_piege():
                resultat = "perdu"
                chrono_fin = millis()
                actuel = "fin"
            elif grille.grille[y][x].get_numero() == 0:
                reveler(x,y)
            else:
                grille.grille[y][x].devoiler()
    if clic=="oui" and origineX <= mouseX <= width-origineX and origineY <= mouseY <= height-origineY and (mouseButton == RIGHT):
        clic="non"
        x,y = entree_joueur()
        if grille.grille[y][x].get_marque():
            grille.grille[y][x].demarquer()
        else:
            grille.grille[y][x].marquer()


def initialisation():
    """
    Réinitialisation des variables nécéssaire au début d'une nouvelle partie.
    """
    global chrono_debut,grille,listImg,taille_case, taille_grille,origineX,origineY,chrono_pause
    chrono_debut = millis()
    chrono_pause = 0
    origineX = (1200-taille_grille[0]*taille_case)/2
    origineY = (600-taille_grille[1]*taille_case)/2
    grille = Grille(taille_grille[1],taille_grille[0],taille_case,(origineY,origineX),listImg)
    grille.nouvelle_grille()

def reveler(x,y):
    """
    Dévoile la case cliqué et appel la fonction sur les cases adjacentes si le numéro =  0.
    x,y : les coordonnées de la case cliquée
    """
    global grille
    grille.grille[y][x].devoiler()
    if grille.grille[y][x].get_numero() == 0 :
        for i in range(-1,2) :
            for j in range(-1,2) :
                if 0 <= x+i < len(grille.grille[y]) and 0 <= y+j < len(grille.grille) :
                    if not grille.grille[y+j][x+i].get_devoile():
                        reveler(x+i,y+j)

def entree_joueur():
    global taille_case,origineX,origineY
    """
    Renvoie les coordonnées de la case cliquée par le joueur. Renvoie None si rien n'est cliqué.
    """
    x = (mouseX - origineX)//taille_case
    y = (mouseY - origineY)//taille_case
    return x,y
    
def partie_terminee(grille):
    """
    Parcours la grille pour verifier si toutes les cases non piégées sont dévoilées.
    Renvoie True ou False.
    """
    for y in range(len(grille.grille)):
        for x in range(len(grille.grille[y])):
            if grille.grille[y][x].get_piege() is False and grille.grille[y][x].get_devoile() is False:
                return False
    return True
            

    
def mousePressed():
    """
    Fonction appelée lorsque le joueur clique.
    """
    global clic
    if clic == "non":
        clic = "oui"
    else:
        clic = "non"

def mouseReleased():
    """
    Fonction appelée lorsque le joueur relache le clique.
    """
    global clic
    clic = "non"
            
