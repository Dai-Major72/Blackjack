import os, sys, cards

deck = cards.shuffle(cards.deck_54(jokers=False))

print(deck, len(deck))
