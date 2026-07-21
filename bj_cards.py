import random
def paquet_52():
    """Créer un paquet de 52 cartes avec les 4 couleurs"""

    global figures
    figures = ["Ace", "Jack", "Queen", "King"]
    paquet = (list(range(2,11)) + figures) * 4
    couleurs = ["\u2665", "\u2660", "\u2666", "\u2663"]
    x = 0
    for carte in range(len(paquet)):
        I = paquet[carte]

        paquet[carte] = str(I) + " " + couleurs[x]
        if "King" in str(I):
            x += 1
    
    random.shuffle(paquet)
    return paquet

def pioche(paquet):
    carte = paquet[-1]
    paquet.pop()
    return carte


def card_value(carte):
    """Tranforme une liste de carte avec couleur en valeur exploitable.
    En considérant que les cartes de 2 à 10 valent leur chiffre, que l'As vaut 1 et quel es figures valent 10
    Ex : "8 ♦" devient un int de 8 """
    valeur = None
    if carte[0:-2] in figures:
        if "Ace" in carte:
            valeur = 1
        else:
            valeur = 10
    else:
        valeur = int(carte[0:2])
    return valeur

rule = """Rules
-
- 2 wins conditions : Score under 22, and higher than the dealer.
- You'll get 2 cards that will get you a score, you can choose to take another card (Hit), or to stop here and let the Dealer start his round (Stay).
- When you stay, and if you didn't Bust (score higer than 21), the Dealer start the same process.
- The Dealer cannot go higher than 21, and will stop drawing cards at 17.
- If the dealer Bust, and you didn't, you win
- If your score's higher than the Dealer's, you win

- Card values : From 2 to 10 cards values are worth their numbers
- Faces are worth 10 (from jack to king)
- Aces are worth either 1 or 11, depends on if your score will go above 21 or not. It will always be shown the highest actual score
- Ex : Ace + king = 21 (11 + 10)
-      Ace + Queen + 5 = 16 (1 + 10 + 5)
-      here the ace is lowered because the max score is too high"""
