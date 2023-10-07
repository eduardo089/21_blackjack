import random

class Deck:
    def __init__(self):
        self.cards = []

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def __str__(self):
        return ", ".join(str(card) for card in self.cards)
