import random
from .card import Card


class Deck:
    def __init__(self) -> None:
        self.cards: list[Card] = []
        self.shapes: list[str] = ["♠", "♣", "♦", "♥"]
        self.values: list[str] = [
            "A",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "J",
            "Q",
            "K",
        ]
        for shape in self.shapes:
            for value in self.values:
                self.cards.append(Card(shape, value))

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def getcard(self) -> Card:
        return self.cards.pop(0)
