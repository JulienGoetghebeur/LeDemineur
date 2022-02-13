#coding=utf-8

#clic = "non"    

def ecran_accueil(img_fond,clic):
    #global clic
    background(0)
    image(img_fond,width//2,height//2,1200,600)
    textSize(75)
    fill(0)
    text("Le demineur",width//2,150,0)
    if bouton_texte(width//2,315,180,60,"Jouer",[0,180,0],40,clic):
        return "jouer"
    if bouton_texte(width//2,400,200,60,"Quitter",[255,0,0],40,clic):
        return "quitter"

def ecran_difficulte(img_fond,clic):
    #global clic
    background(0)
    image(img_fond,width//2,height//2,1200,600)
    textSize(40)
    fill(0)
    text("Choissisez votre difficulte :",width//2,150,0)
    if bouton_texte(width//2,250,250,60,"Debutant",[0,180,0],40,clic):
        return "débutant"
    if bouton_texte(width//2,350,340,60,"Intermediaire",[255,131,0],40,clic):
        return "intermédiaire"
    if bouton_texte(width//2,450,230,60,"Difficile",[255,0,0],40,clic):
        return "difficile"

def ecran_pause(clic):
    #global clic
    textSize(75)
    fill(0)
    rect(width//2,height//2,400,400,10)
    fill(255)
    text("Pause",width//2,190,0)
    if bouton_texte(width//2,275,260,60,"Reprendre",[0,180,0],40,clic):
        return "reprendre"
    if bouton_texte(width//2,350,320,60,"Recommencer",[0,0,255],40,clic):
        return "recommencer"
    if bouton_texte(width//2,425,200,60,"Quitter",[255,0,0],40,clic):
        return "quitter"

def ecran_fin(img_gagne, resultat,chrono,img_perdu,clic):
    #global clic
    if resultat == "gagné":
        background(0)
        image(img_gagne,width/2,height/2,1200,600)
        fill(0)
        textSize(50)        
        text("Votre score : " + str(chrono),900,200,0)        
        if bouton_texte(900,275,245,60,"Rejouer",[0,180,0],50,clic):            
            return "rejouer"        
        if bouton_texte(900,350,237,60,"Quitter",[255,0,0],50,clic):            
            return "quitter"
    if resultat == "perdu":
        background(0)
        fill(0)
        image(img_perdu,width//2,height//2,1200,600)
        textSize(50)
        text("Votre score : " + str(chrono),790,275,0)
        if bouton_texte(790,375,245,60,"Rejouer",[0,180,0],50,clic):
            return "rejouer"
        if bouton_texte(790,450,237,60,"Quitter",[255,0,0],50,clic):
            return "quitter"

def ecran_jeu(img_jeu,img_bouton_pause,chrono,clic):
    #global clic
    background(0)
    image(img_jeu,width/2,height/2,1200,600)
    textSize(50)
    fill(255)
    text("Score : " + str(chrono),width//2,50)
    #rect(width//2,325,1100,500)
    if bouton_image(img_bouton_pause,width-40,40,32,32,clic):
        return "pause"
    
        

def bouton_texte(x,y,largeur,hauteur,texte,couleur,taille_ecriture,clic):
    #global clic
    """    
    Fonction qui affiche un bouton qui affiche un contour quand la souris passe dessus.
    x,y : coordonnées du bouton
    largeur,hauteur : dimension du bouton
    couleur : couleur du bouton
    taille_ecriture : taille de la police 
    """ 
    textSize(taille_ecriture)   
    if  x - largeur/2 < mouseX < x + largeur/2 and  y-hauteur/2 < mouseY < y + hauteur/2 :  
        noFill()      
        stroke(couleur[0],couleur[1],couleur[2])
        strokeWeight(5)
        rect(x,y,largeur,hauteur,20) 
        noStroke()
        fill (couleur[0],couleur[1],couleur[2])                    
        text(texte,x,y+hauteur*0.28)     
        if clic == "oui" :  
            clic = "non"          
            return True
    else:        
        fill(couleur[0],couleur[1],couleur[2])          
        text(texte,x,y+hauteur*0.28)    
    return False

def bouton_image(img,x,y,largeur,hauteur,clic):
    #global clic
    """
    Fonction qui affiche un bouton-image qui grandi quand la souris passe dessus.
    img : image du bouton    
    x,y : coordonnées du bouton    
    largeur,hauteur : dimension du bouton    
    """    
    if  x - largeur/2 < mouseX < x + largeur/2 and  y-hauteur/2 < mouseY < y + hauteur/2 :
        image(img,x,y,largeur+10,hauteur+10)
        if clic == "oui" :
            clic = "non"           
            return True    
    else:
        image(img,x,y,largeur,hauteur)
        return False
    
    
    

# def mousePressed():
#     global clic
#     if clic == "non":
#         clic = "oui"
#     else:
#         clic = "non"
