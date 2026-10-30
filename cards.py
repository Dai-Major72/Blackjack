import random

faces = ["Jack", "Queen", "King","Ace"]

colors = {
    "heart":"\u2665",
    "spade":"\u2660",
    "diamond":"\u2666",
    "club":"\u2663"
}

def deck_54(ace_is_one=False,jokers=True,faces_value=0):
    # Return a dict of 54 values, one for each card
    # Default values order : 2 < 10 < J < Q < K < A
    # Args : ace_is_one to tell if Aces should be the lowest or highest card
    #        jokers to add or remove 2 Jokers
    #        faces_values to make faces equals to the chosen value. (Doesn't affect the Ace)
    def value(card):

        if card in faces:
            if not faces_value : return [11,12,13,1 if ace_is_one else 14][faces.index(card)]
            elif card != "Ace" : return faces_value
            else : return 1 if ace_is_one else 14

        else: return int(card)

    blank = list(range(2,11)) + faces
    deck = {}
    for logo in colors.values():
        for card in blank:
            deck.update({f"{card} {logo}":value(card)})
    if jokers : deck.update({"Joker 1":15, "Joker 2":15})
    return deck

def draw(deck):
    #Return a card and remove it from the deck.
    return deck.popitem()

def shuffle(deck):
    # Shuffle the given deck.
    card_list = list(deck.items())
    random.shuffle(card_list)
    return dict(card_list)
