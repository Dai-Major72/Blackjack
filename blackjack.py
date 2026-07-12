#!/bin/python3

from modules import Paquet52, ValeurCarte
from time import sleep
import sys
from os import environ as env
from pathlib import Path


Paquet = Paquet52()
save_file_path = env['HOME'] + "/.blackjack_save"
if Path(save_file_path).is_file() == False:
    with open(save_file_path, "x") as saveCreate:
        saveCreate.write("Blackjack Bank\n")

def Save(Joueur):
    print("Save..")
    player_save = f"{Joueur.nom} = argent : {Joueur.argent}\n"
    InSave = False
    with open(save_file_path, "rt") as save:
        cache = save.read()
        for line in cache.splitlines():
            if Joueur.nom == line.split(" =")[0]:
                cache = cache.replace(line, player_save)
                with open(save_file_path, "w") as saveW:
                    saveW.write(cache)
                InSave = True
                break

        if InSave != True:
            with open(save_file_path, "a") as saveA:
                saveA.write(player_save)

def Pioche():
    carte = Paquet[-1]
    Paquet.pop()
    return carte

def Points(Joueur):
    pts = 0
    As_Count = 0
    for carte in Joueur.cartes:
        if ValeurCarte(carte) == 1:
            As_Count += 1
        else:
            pts += ValeurCarte(carte)
    for As in range(As_Count):
        if pts + 11 > 21:
            pts += 1
        else: pts += 11
    return pts

def Bust(Joueur):

    if Points(Joueur) > 21:
        return True
    else: 
        return False

def Init_Player():
    global Bob
    Bob = Joueur()

def Start():
    Bob.Hit()
    Dealer.Hit()
    Bob.Hit()

def menu(Joueur):


    while True:
        m = str(input(f"{Joueur.Balance()}\n[1] Miser\n[2] Changer de joueur\n[3] Quitter\n"))
        if m == "1":
            Bob.Mise()
            break
        elif m == "2":
            Bob.exit()
            Dealer.exit()
            return "Back"
        elif m == "3":
            print("A bientot :)")
            sys.exit()



def CardReset():
    Bob.cartes = []
    Dealer.cartes = []

def Get_Player_Money(Joueur):
    with open(save_file_path, "r") as save:
        for line in save:
            if Joueur.nom == line.split(" = ")[0]:
                return int(line.split(" ")[-1])
        return 1000

class Joueur:
    
    def __init__(self):
        self.nom = str(input("Nom :\n"))
        self.argent = Get_Player_Money(self)
        self.cartes = []
        
    def Hit(self):
        self.cartes.append(Pioche())

    def Cartes(self):
        print(f"{self.nom}\n{self.cartes} = {Points(self)}\n")

    def Balance(self):
        return f"Argent [{self.argent}]"
        
    def Mise(self):
        if self.argent <= 0:
            print("Vous êtes fauché !")
            print("Faveur de la banque, prenez 1000")
            self.argent = 1000
            Save(self)
        self.mise = 0
        while self.mise == 0:
            print(self.Balance())
            self.mise = input("Mise :")
            if self.mise.isdigit() == False:
                self.mise = 0
            else: self.mise = int(self.mise)
        self.argent -= self.mise
        print(self.Balance())

    def Win(self):
        self.argent += self.mise * 2
        Dealer.argent -= self.mise
        
    def Egalite(self):
        self.argent += self.mise

    def exit(self):
        del self
class Dealer(Joueur):

    def __init__(self):
        self.argent = 999999
        self.nom = "Dealer"
        self.cartes = []

    def Cartes(self):
        super().Cartes()
    def Hit(self):
        super().Hit()

    def Win(self, joueur):
        self.argent += joueur.mise

    def exit(self):
        del self

Dealer = Dealer()

while True: #Jeu

    Init_Player()
    
    while True: #Tour de jeu

        Save(Bob)
        if menu(Bob) == "Back":
            break
        Paquet = Paquet52()
        Start()

        while Bust(Bob) != True: #Tour du joueur

            Dealer.Cartes()
            Bob.Cartes()
            g = None
            while g not in ["O", "", "n"]:
                g = str(input("Hit ? O/n"))

            if g == "O" or g == "":
                Bob.Hit()
                Bob.Cartes()
            else:
                print(f"{Bob.nom} reste !")
                break
            
            if Bust(Bob):
                print(f"{Bob.nom} a Bust !")
                    
        while Bust(Dealer) != True and Bust(Bob) != True: #Tour du Dealer

            Dealer.Hit()
            Dealer.Cartes()
            sleep(1)
            if Points(Dealer) >= 17:
                if Bust(Dealer):
                    print("Le Dealer a Bust !")
                break         

        if Bust(Bob):
            print("Le Dealer gagne !")
            Dealer.Win(Bob)

        elif Bust(Dealer):
            print(f"{Bob.nom} gagne !")
            Bob.Win()
            
        else:
            if Points(Bob) > Points(Dealer):
                print(f"{Bob.nom} gagne aux pts !")
                Bob.Win()
            elif Points(Bob) < Points(Dealer):
                print("Le Dealer gagne aux pts")
                Dealer.Win(Bob)
            else:
                print("Egalité !")
                Bob.Egalite()
                
        CardReset()
#A faire :
# - Faire un affichage propre (pygame un jour ?)
#
# - Reset de l'argent du Dealer ? Ou système de banque infinie ?
# - Optimiser le code (fonctions, et boucle principale)
