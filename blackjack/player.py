from hand import Hand
from chip import Chip


class Player:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.hand: Hand = Hand()
        self.chip: Chip = Chip()

    def placeBet(self, bet: int) -> bool:
        if self.chip.chip < bet:
            print(f"Kindly reduce bet amount than: {self.chip.chip}")
            return False
        else:
            self.chip.modbet(bet)
            return True

    def win(self) -> None:
        self.chip.betwin()

    def lose(self) -> None:
        self.chip.betlos()

    def emptyHand(self) -> None:
        self.hand = Hand()
