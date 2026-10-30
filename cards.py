#from random import randint

faces = ["Jack", "Queen", "King","Ace"]

colors = {
    "heart":"\u2665",
    "spade":"\u2660",
    "diamond":"\u2666",
    "club":"\u2663"
}

def deck_54(ace_is_one=False,jokers=False,faces_value=0):

    def value(card):
        if card in faces and faces_value: return faces_value
        elif card in faces: return [1 if ace_is_one else 11,12,13,14][faces.index(card)]
        else: return int(card)

    hand = list(range(2,11)) + faces
    deck = {}
    for logo in colors.values():
        for card in hand:
            deck.update({f"{card} {logo}":value(card)})
    if jokers : deck.update({"Joker 1":15, "Joker 2":15})
    return deck




    """Return a dict of a 54 (or 52) card deck. Every color.
    Card value : 2 < 10 < J < Q < K < A
    Dict entrys are : 'card name + color':card_value_as_int

    Args : ace_is_one : if True, ace is weaker than 2. Default Ace is the strongest card
           jokers : define if jokers will be in the deck. if set to false, return a 52 cards deck.
           faces_value : if set to an int,  all faces will be equals with this value Default faces values are 11, 12 and 13
    """
print(deck_54(True,True,12))
