import save_manager as sm
import cards

def player_money(player_class):
    return player_class.fetch()["money"]

default_save = {"money": 1000}

class Default_player:

    def __init__(self):
        self.name = str(input("Enter player name : "))
        self.class_save_file = sm.save(self.name)
        if not self.class_save_file.do_exist():
            self.class_save_file.create(); self.class_save_file.write(default_save)
            print("Player found")
        self.money = player_money(self.class_save_file)
        self.cards = {}
        self.bet = 0


    def hit(self,deck):
        self.cards.update({cards.draw(deck)})

    def show_cards(self): #Return card list in hand
        return list(self.cards.keys())

    def sum_cards(self): # Return sum of cards in hand
        return sum(self.cards.values())

class Default_dealer(Default_player):

    def __init__(self):
        self.name = "Dealer"
        self.cards = {}
