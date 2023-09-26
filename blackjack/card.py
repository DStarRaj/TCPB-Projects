class Card:
    value_map = {
        "A": 11,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "Q": 10,
        "K": 10,
    }

    def __init__(self, shape: str, value: str) -> None:
        self.__shape = shape
        self.__value = value
        self.isA = False
        if self.__value == "A":
            self.isA = True

    def __str__(self) -> str:
        return f"{self.__shape} {self.__value}"

    def __repr__(self) -> str:
        return self.__str__()

    @property
    def rank(self) -> int:
        return self.value_map[self.__value]
