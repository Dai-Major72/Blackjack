from random import randint

figures = ["Ace", "Jack", "Queen", "King"]
colors = {"heart":"\u2665", "spike":"\u2660",
        "diamond":"\u2666", "clove":"\u2663"}
def deck_54(ace_is_one=False,jokers=False,figures_value=False):
    """Return a dict of a 54 (or 52) card deck. Every color.
    Card value : 2 < 10 < J < Q < K < A
    Dict entrys are : 'card name + color':card_value_as_int
    
    Args : ace_is_one : if True, ace is weaker than 2. Default Ace is the strongest card
           jokers : define if jokers will be in the deck. if set to false, return a 52 cards deck.
           figures_value : if set to an int,  all figures will be equals with this value Default figures values are 11, 12 and 13
    """
    ...
