# Ida's Tic Tac Toe!  

Welcome to my Python console based version of Tic Tac Toe that allows two human players to play on a 3 x 3 board.

## How to run

1. Download this awesome tictactoe using `git clone https://github.com/idaknow/TicTacToe-MYOBCodingProblem.git`.
2. Ensure [Python3](https://www.python.org/downloads/) is downloaded on your computer 
3. Run the tictactoe.py file in the tictactoe package, for example `python3 tictactoe/tictactoe.py`

## How to play Tic Tac Toe

The instructions to run the file will begin the crazy fun tictactoe game!!

Each player is given a turn to input coordinates of the 2D board to place their X or O:

```
. . .

. . .

. . .
```

For example, if Player 1 inputs the co-ordinated 1,1 the new board will look like:

```
X . .

. . .

. . .
```

Now it's the turn of Player 2 to input their co-ordinates. The aim of the game is to try and win by getting 3 of your moves in a row, column or diagonal. It's a draw if the whole board gets full up, but no one has explicitly won a row, column or diagonal.You can quit the game at any time by inputting 'q'.

**HAVE FUN**

### File Structure

The tictactoe python package contains four files:

* tictactoe.py: This is the file that calls the other classes to start the tictactoe game.
* main_game.py: This class contains all the main functionality for the game, that is called on by tictactoe.py
* board.py: This class contains all the information about the status of the game board.
* player.py: This class contains the status of which player is currently playing

## My assumptions

* I have assumed a basic knowledge of tictactoe, and therefore have not included instructions in the console game apart from adding the co-ordinates. The players switch each turn, which I assumed the players knew.
* I have assumed the players have a basic knowledge on co-ordinates, such as 1,1 representing the first place, and 3,3 representing the last place. However, I have created different error messages for different input mistakes to help this and an example in my readme.
* I have assumed no one "wins" if someone presses q to give up the game.
