#!/usr/bin/python
import sys

PLAYER_1_MOVE="X"
PLAYER_2_MOVE="O"

class Player:

    def __init__(self):
        self.player_number = 1;
        self.player_move = PLAYER_1_MOVE;

    # Adds the player's X or O (depending on which player) to the board
    def switch_player(self):
        if self.player_number == 2:
            self.player_move = PLAYER_1_MOVE;
            self.player_number = 1; # Decrement player from 2 to 1
        else:
            self.player_move = PLAYER_2_MOVE;
            self.player_number = 2; # Increment player from 1 to 2

    def get_player_number(self):
        return self.player_number;

    def get_player_move(self):
        return self.player_move;
