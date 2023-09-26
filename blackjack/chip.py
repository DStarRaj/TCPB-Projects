class Chip:
    def __init__(self) -> None:
        self.chip: int = 100
        self.bet: int = 0

    def modbet(self, bet: int) -> None:
        self.bet = bet

    def betwin(self) -> None:
        self.chip += self.bet

    def betlos(self) -> None:
        self.chip -= self.bet
