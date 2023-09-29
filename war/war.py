from dataclasses import dataclass, field
import random


@dataclass
class Card:
    shape: str
    value: str
    rank: int = field(init=False)

    def __post_init__(self) -> None:
        self.value_map = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "J": 11,
            "Q": 12,
            "K": 13,
            "A": 14,
        }
        self.rank = self.value_map[self.value]

    def __str__(self) -> str:
        return f"{self.shape} {self.value}"

    def __repr__(self) -> str:
        return self.__str__()

    def __lt__(self, card: "Card") -> bool:
        return self.rank < card.rank

    def __le__(self, card: "Card") -> bool:
        return self.rank <= card.rank

    def __eq__(self, card: "Card") -> bool:
        return self.rank == card.rank

    def __ne__(self, card: "Card") -> bool:
        return self.rank != card.rank

    def __gt__(self, card: "Card") -> bool:
        return self.rank > card.rank

    def __ge__(self, card: "Card") -> bool:
        return self.rank >= card.rank


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


class Player:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.card_stack: list[Card] = []

    def add_card(self, card: Card) -> None:
        self.card_stack.append(card)

    def get_card(self) -> Card:
        return self.card_stack.pop(0)

    def len(self) -> int:
        return len(self.card_stack)


def main():
    deck = Deck()
    deck.shuffle()
    deck.shuffle()
    deck.shuffle()

    playerA = Player(input("Enter player1's name: "))
    playerB = Player(input("Enter player2's name: "))

    for idx, card in enumerate(deck.cards):
        if idx % 2 == 0:
            playerA.add_card(card)
        else:
            playerB.add_card(card)

    game: bool = True
    while game:
        curr_stack: list[Card] = []
        pAc: Card = playerA.get_card()
        pBc: Card = playerB.get_card()
        curr_stack.append(pAc)
        curr_stack.append(pBc)
        print(f"{playerA.name} plays {pAc}, has left {playerA.len()}")
        print(f"{playerB.name} plays {pBc}, has left {playerB.len()}")
        stack_winner: Player
        war: bool = False
        if pAc > pBc:
            stack_winner = playerA
        elif pBc > pAc:
            stack_winner = playerB
        else:
            war = True
        while war:
            print("In War")
            for _ in range(3):
                if playerA.len():
                    curr_stack.append(playerA.get_card())
                else:
                    war = False
                    break
                if playerB.len():
                    curr_stack.append(playerB.get_card())
                else:
                    war = False
                    break

            if playerA.len():
                pAc = playerA.get_card()
            else:
                stack_winner = playerB
                war = False
                break
            if playerB.len():
                pBc = playerB.get_card()
            else:
                stack_winner = playerA
                war = False
                break

            curr_stack.append(pAc)
            curr_stack.append(pBc)
            print(f"{playerA.name} plays {pAc}, has left {playerA.len()}")
            print(f"{playerB.name} plays {pBc}, has left {playerB.len()}")
            if pAc > pBc:
                stack_winner = playerA
                war = False
            elif pBc > pAc:
                stack_winner = playerB
                war = False

        print(f"{stack_winner.name} gets {curr_stack}")
        for card in curr_stack:
            stack_winner.add_card(card)
        print()

        if playerA.len() == 0 or playerB.len() == 0:
            game = False

    if playerA.len():
        print(f"{playerA.name} wins the game !!!")
    else:
        print(f"{playerB.name} wins the game !!!")


if __name__ == "__main__":
    main()
