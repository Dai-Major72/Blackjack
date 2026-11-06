import save_manager as sm

def player_money(player_class):
    return player_class.fetch()["money"]

class Player:

    def __init__(self, base_money=1000):
        self.name = str(input("Enter player name : "))
        self.save_file = sm.save(player_class_name=self.name)
        (self.save_file.create(), self.save_file.write({"money" : base_money})) if not self.save_file.do_exist() else print("Player found")
        self.money = player_money(self.save_file) if self.save_file.do_exist() else base_money

Joueur1 = Player()
print(Joueur1.money)
