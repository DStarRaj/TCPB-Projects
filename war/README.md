# War

[War](https://en.wikipedia.org/wiki/War_(card_game)) (_also known as **Battle** in the United Kingdom_) is a simple card game, typically played by two players using a standard playing card deck.

In this project I have made the representation of a War Game played between two computer players.

## Game Logic
The game logic is pretty simple and easy to understand.

* The deck is divided evenly among the players, giving each a down stack.
* In unison, each player reveals the top card of their deck.
* The player with the higher card takes both of the cards played and moves them to their bottom of the stack.
* If the two cards played are of equal value, then there is a **war**.
  * Both players place the next 3 cards from their pile separately and then another card face-up.
  * The owner of the higher face-up card wins the war and adds all the cards on the table to the bottom of their deck.
  * If the face-up cards are again equal then the battle repeats with another set of separate and face-up cards.
* Once a player has all the 52 cards, he/she's considered winner.

## Implementation
In my variation of the game, the game is based on two computer players and it is more of a simulation rather than a "actual game". It's a CLI based game and can be run with python installed on system with no other libraries needed.

### Running the Game
```bash
python war.py
```

### Inputs to the Game
For visual representation and for the sake of Game enjoyments, it asks for the two players name which is needed as input to the Game and nothing else, not the program will run it's simulation to evaluate who is the winner.

### Somthing to keep in mind
In this simulation of the game, outcomes are entirely dictated by the random distribution of cards to players. A player's chance of winning is solely dependent on this randomness, not on their skills. This factor significantly influences the game's progression and duration; based on my tests, specific distributions can make the game last much longer.