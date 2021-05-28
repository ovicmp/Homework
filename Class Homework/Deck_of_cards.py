import itertools
import random


class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print(f"{self.value} of {self.suit}")


class Deck():
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suits in ["Hearts", "Bells", "Acorns", "Leaves"]:
            for value in [2, 3, 4, 7, 8, 9, 10, 11]:
                print(f"{suits} of {value}")


deck1 = Deck()

card = Card("Bells", 7)
card.show()
