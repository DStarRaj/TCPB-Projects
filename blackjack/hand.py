from card import Card


class Hand:
    def __init__(self) -> None:
        self.stack: list[Card] = []
        self.Acount: int = 0

    def add_card(self, card: Card) -> None:
        self.stack.append(card)
        if card.rank == 11:
            self.Acount += 1

    def getAllSum(self) -> list[int]:
        sums = []
        base_sum = 0
        for each in self.stack:
            base_sum += each.rank
        sums.append(base_sum)
        for each in range(self.Acount):
            base_sum -= 10
            sums.append(base_sum)
        return sums

    def getMinSum(self) -> int:
        return min(self.getAllSum())

    def getNear21(self) -> int:
        allSum = self.getAllSum()
        near21 = self.getMinSum()
        for each in allSum:
            if each > near21 and each <= 21:
                near21 = each
        return near21

    def len(self) -> int:
        return len(self.stack)
