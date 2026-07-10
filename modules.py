import random
def Paquet52():
    
    global figures
    figures = ["As", "Valet", "Dame", "Roi"]
    Paquet = list(range(2,11))
    Paquet.extend(figures)
    Paquet.extend(Paquet * 3)
    couleurs = ["\u2665", "\u2660", "\u2666", "\u2663"]
    x = 0
    for carte in range(len(Paquet)):
        I = Paquet[carte]

        Paquet[carte] = str(I) + " " + couleurs[x]
        if "Roi" in str(I):
            x += 1
    
    random.shuffle(Paquet)
    return Paquet
#Transforme les cartes du Paquet en valeur exploitable

def ValeurCarte(carte):
    valeur = None
    if carte[0:-2] in figures:
        if "As" in carte:
            valeur = 1
        else:
            valeur = 10
    else:
        valeur = int(carte[0:2])
    return valeur
