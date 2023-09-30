from utilities.deck import Deck
from utilities.player import Player


def displayHands(dealer: Player, player: Player, showDealer: bool = False) -> None:
    print()
    if showDealer:
        print(
            f"{dealer.name} has {dealer.hand.len()} cards with val {dealer.hand.getNear21()}:"
        )
        print(dealer.hand.stack)
    else:
        print(f"{dealer.name} has {dealer.hand.len()} cards")
        print([dealer.hand.stack[0], "card hidden"])
    print(
        f"{player.name} has {player.hand.len()} cards with val {player.hand.getNear21()}:"
    )
    print(player.hand.stack)
    print()


def gameLoop(player: Player) -> bool:
    deck = Deck()
    deck.shuffle()

    ## Initialiazation
    dealer = Player("Dealer")
    hit: bool = True
    play: bool = True

    ## Starting Hand
    dealer.hand.add_card(deck.getcard())
    dealer.hand.add_card(deck.getcard())
    player.hand.add_card(deck.getcard())
    player.hand.add_card(deck.getcard())

    ## Hit or Stand
    while hit:
        displayHands(dealer, player)

        ## Check if player wins
        if player.hand.getNear21() == 21:
            print(f"Congrat's {player.name} you've scored a perfect 21.")
            play = False
            return True

        ## Check if player loses
        if player.hand.getMinSum() > 21:
            print(f"Oops, you lost this round.")
            play = False
            return False

        print("Do you want to 1. Hit or 2. Stand?")
        flag = input("Enter (1) or (2): ")
        if flag == "1":
            player.hand.add_card(deck.getcard())
        elif flag == "2":
            hit = False
        else:
            print("Invaild response, try again...")
            continue

    ## Dealer's hand
    while play:
        displayHands(dealer, player, showDealer=True)

        ## Check if dealer loses
        if dealer.hand.getMinSum() > 21:
            print(f"Congrat's {player.name} you've won this round.")
            return True

        ## Check if dealer wins
        if (
            dealer.hand.getNear21() <= 21
            and dealer.hand.getNear21() > player.hand.getNear21()
        ):
            print(f"Oops, {dealer.name} scored more than you.")
            return False

        card = deck.getcard()
        print(f"{dealer.name} draws {card}")
        dealer.hand.add_card(card)


def main() -> None:
    ## Initialise Player
    player = Player(input("Enter your name: "))
    round: int = 1

    game = True
    while game:
        bet = int(input("Enter bet amount: "))
        if not player.placeBet(bet):
            continue
        player.emptyHand()
        win = gameLoop(player)
        if win:
            player.win()
        else:
            player.lose()

        money = player.chip.chip
        print(f"After round {round} you have {money}")

        if money == 0:
            print("Sorry, you wont be able to play more...")
            game = False
            break

        while True:
            print("Do you want to play more?")
            flag = input("Enter (1) Yes or (2) No: ")
            if flag == "1":
                game = True
                break
            elif flag == "2":
                game = False
                break
            else:
                print("Invaild response, try again...")
                continue

        round += 1


if __name__ == "__main__":
    main()
