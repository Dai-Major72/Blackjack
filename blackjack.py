#!/bin/python3

from bj_cards import paquet_52, card_value, rule, pioche
from time import sleep
import sys
import os
from pathlib import Path


paquet = paquet_52()
save_file_path = os.environ['HOME'] + "/.blackjack_save"
if Path(save_file_path).is_file() == False:
    with open(save_file_path, "x") as saveCreate:
        saveCreate.write("Blackjack Bank\n")

def save(Joueur):
    print(f"Saved {Joueur.nom}")
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

def points(Joueur):
    pts = 0
    as_count = 0
    for carte in Joueur.cartes:
        if card_value(carte) == 1:
            as_count += 1
        else:
            pts += card_value(carte)
    for As in range(as_count):
        if pts + 11 > 21:
            pts += 1
        else: pts += 11
    return pts

def is_bust(Joueur):
    return points(Joueur) > 21

def init_player():
    global Bob
    Bob = Joueur()

def start():
    Bob.hit()
    Dealer.hit()
    Bob.hit()

def clean():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu(Joueur):

    while True:
        m = str(input(f"{Joueur.balance()}\n[1] Bet\n[2] Change player\n[3] Rules\n[4] Quit\n"))
        clean()
        if m == "1":
            Bob.bet()
            break
        elif m == "2":
            Bob.exit()
            Dealer.exit()
            return "Back"
        elif m == "3":
            print(rule)
        elif m == "4":
            print("A bientot :)")
            sys.exit()

def table_screen(Joueur, Dealer):
    clean()
    print(f"{Joueur.balance()}\nBet [{Joueur.mise}]")
    Dealer.show_cards()
    Joueur.show_cards()

def card_reset():
    Bob.cartes = []
    Dealer.cartes = []

def get_player_money(Joueur):
    with open(save_file_path, "r") as save:
        for line in save:
            if Joueur.nom == line.split(" = ")[0]:
                return int(line.split(" ")[-1])
        return 1000

class Joueur:
    
    def __init__(self):
        self.nom = str(input("Name : "))
        self.argent = get_player_money(self)
        self.cartes = []
        self.mise = 0
        
    def hit(self):
        self.cartes.append(pioche(paquet))

    def show_cards(self):
        print(f"{self.nom}\n{self.cartes} = {points(self)}\n")

    def balance(self):
        return f"Money [{self.argent}]"
        
    def bet(self):
        if self.argent <= 0:
            print("You are broke !")
            print("Banks favor, take 1000")
            self.argent = 1000
            save(self)
        self.mise = 0
        while True:
            print(self.balance())
            self.mise = input("Bet : ")
            if self.mise.isdigit() == False:
                continue
            elif int(self.mise) > self.argent:
                print("You don't have enough money")
                continue
            else:
                self.mise = int(self.mise)
                break
        self.argent -= self.mise
        print(self.balance())

    def win(self):
        self.argent += self.mise * 2
        Dealer.argent -= self.mise
        
    def egalite(self):
        self.argent += self.mise

    def exit(self):
        del self
class Dealer(Joueur):

    def __init__(self):
        self.argent = 999999
        self.nom = "Dealer"
        self.cartes = []

    def show_cards(self):
        super().show_cards()

    def hit(self):
        super().hit()

    def win(self, joueur):
        self.argent += joueur.mise

    def exit(self):
        del self

Dealer = Dealer()

while True: #Jeu

    clean()
    init_player()
    
    while True: #Tour de jeu

        clean()
        save(Bob)
        if menu(Bob) == "Back":
            break
        paquet = paquet_52()
        start()

        while is_bust(Bob) != True: #Tour du joueur

            table_screen(Bob,Dealer)

            g = None
            while g not in ["Y", "", "n"]:
                g = str(input("Hit ? Y/n "))

            if g == "Y" or g == "":
                Bob.hit()
            else:
                print(f"\n{Bob.nom} stays !")
                sleep(2)
                break
            
            if is_bust(Bob):
                table_screen(Bob, Dealer)
                print(f"\n{Bob.nom} busted !")
                sleep(1)
                    
        while is_bust(Dealer) != True and is_bust(Bob) != True: #Tour du Dealer

            Dealer.hit()
            table_screen(Bob, Dealer)
            sleep(2)
            if points(Dealer) >= 17:
                if is_bust(Dealer):
                    print("Dealer busted !")
                break         

        if is_bust(Bob):
            print("Dealer wins")
            Dealer.win(Bob)

        elif is_bust(Dealer):
            print(f"{Bob.nom} wins !")
            Bob.win()
            
        else:
            if points(Bob) > points(Dealer):
                print(f"{Bob.nom} wins!")
                Bob.win()
            elif points(Bob) < points(Dealer):
                print("Dealer wins !")
                Dealer.win(Bob)
            else:
                print("Draw !")
                Bob.egalite()
                
        card_reset()
        sleep(2)
#A faire :
# - Faire un affichage propre (pygame un jour ?)
#
# - Optimiser le code (fonctions, et boucle principale)
