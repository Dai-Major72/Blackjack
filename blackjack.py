#!/bin/python3

from bj_cards import paquet_52, card_value, card_name, rule, pioche
import save_manager as sm
from time import sleep
import sys
import os


paquet = paquet_52()
sm.create_save_file(os.environ['HOME'] + "/.blackjack_save", "Blackjack Bank")

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
        self.mise = 0
        if self.argent <= 0:
            print("You are broke !")
            print("Banks favor, take 1000")
            self.argent = 1000
            save(self)
        while True:

            print(self.balance())
            try:
                self.mise = int(input("Bet : "))
            except ValueError:
                print("That is not a correct bet")
                clean(2)
                continue
            if self.mise > self.argent:
                print("You don't have enough money")
                clean(2)
                continue
            else:
                break
        self.argent -= self.mise

    def double_bet(self):
        while self.argent >= self.mise * 2:
            self.argent -= self.mise
            self.mise += self.mise
            return True
        return False

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

def get_player_money(Joueur):
    with open(sm.save_file, "r") as save:
        for line in save:
            if Joueur.nom == line.split(" = ")[0]:
                return int(line.split()[-1][0:-3])
        return 1000

def init_player():
    global Player
    Player = Joueur()
init_player()

def points(Joueur):
    pts = 0
    ace_count = 0
    for carte in Joueur.cartes:
        if card_value(carte) == 1:
            ace_count += 1
        else:
            pts += card_value(carte)
    for As in range(ace_count):
        if pts + 11 > 21:
            pts += 1
        else: pts += 11
    return pts

def is_bust(Joueur):
    return points(Joueur) > 21

def split_check(Joueur):
    if card_name(Joueur.cartes[0]) == card_name(Joueur.cartes[1]): return True

def start():
    Player.hit()
    Dealer.hit()
    Player.hit()

def clean(time_before_sleep=0):
    sleep(time_before_sleep)
    os.system('cls' if os.name == 'nt' else 'clear')

def menu(Joueur):

    while True:
        m = str(input(f"{Joueur.balance()}\n[1] Bet\n[2] Change player\n[3] Rules\n[4] Quit\n"))
        clean()
        if m == "1":
            Player.bet()
            break
        elif m == "2":
            Player.exit()
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

def turn_menu(Joueur):
    while True:
        table_screen(Player, Dealer)
        if len(Joueur.cartes) <= 2:
            m = str(input("[1] Hit     [2] Stay    [3] Double "))
        else:
            m = str(input("[1] Hit     [2] Stay "))

        if m == "1":
            Player.hit()
            table_screen(Player, Dealer)
            break
        elif m == "2":
            print(f"{Joueur.nom} stays !")
            sleep(2)
            return False
        elif m == "3":
            if len(Joueur.cartes) <= 2:
                if Player.double_bet():
                    Player.hit()
                    table_screen(Player, Dealer)
                    print("You double your bet")
                    print(f"{Joueur.nom} can't hit anymore")
                    sleep(2)
                    if is_bust(Player):
                        print(f"\n{Player.nom} busted !")
                        sleep(2)
            else:
                continue
            return False
        table_screen(Player,Dealer)
    return True

def card_reset():
    Player.cartes = []
    Dealer.cartes = []

Dealer = Dealer()

while True: #Jeu

    clean()

    while True: #Tour de jeu

        clean()
        sm.save(Player.nom, f"argent : {Player.argent}")
        if menu(Player) == "Back":
            init_player()
            break
        paquet = paquet_52()
        start()

        table_screen(Player,Dealer)

        while turn_menu(Player): #Tour du joueur

            if is_bust(Player):
                print(f"\n{Player.nom} busted !")
                sleep(2)
                break

        while not is_bust(Dealer) and not is_bust(Player) : #Tour du Dealer

            Dealer.hit()
            table_screen(Player, Dealer)
            sleep(2)
            if points(Dealer) >= 17:
                if is_bust(Dealer):
                    print("Dealer busted !")
                break

        if is_bust(Player):
            print("Dealer wins")
            Dealer.win(Player)

        elif is_bust(Dealer):
            print(f"{Player.nom} wins !")
            Player.win()

        else:
            if points(Player) > points(Dealer):
                print(f"{Player.nom} wins!")
                Player.win()
            elif points(Player) < points(Dealer):
                print("Dealer wins !")
                Dealer.win(Player)
            else:
                print("Draw !")
                Player.egalite()

        card_reset()
        sleep(2)
#A faire :
# - Faire un affichage propre (pygame un jour ?)
#
# - Optimiser le code (fonctions, et boucle principale)
