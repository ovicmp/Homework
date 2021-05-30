from random import shuffle
from pprint import pprint as pp


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        suits = ['Hearts', 'Bells', 'Acorns', 'Leaves']
        values = ['2', '3', '4', '7', '8', '9', '10', '11']
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def __repr__(self):
        return f"Cards remaining in deck: {len(self.cards)}"

    def shuffle(self):
        if len(self.cards) < 32:
            raise ValueError("Can shuffle cards only with a full deck of 32!")
        shuffle(self.cards)
        return self

    def deal(self):
        if len(self.cards) == 0:
            raise ValueError("All cards have been dealt")
        return self.cards.pop()


def __main__():
    my_deck = Deck()
    pp(my_deck.shuffle())
    print('The card you got is: ', my_deck.deal())
    # pp(my_deck.shuffle()) - 'if this is run then value error is raised'
    print(my_deck.__repr__())

__main__()
