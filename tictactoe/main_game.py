#!/usr/bin/python
import sys

from board import Board;
from player import Player;

# Welcome to Ida's TicTacToe!

#TODO: ADD MORE ERROR MESSAGES
ERROR_MESSAGES=["\nSorry, we could not recognise your input. Please try again!\n","\nSomeone is already at this position! Please try again\n"]
COMMA=","
PLAYER_QUIT="q"

class TicTacToe:

    # Initialises the tictactoe board, players and index values
    def __init__(self):
        self.board = Board();
        self.player = Player();
        self.i = 0; # indexes of the players coordinates
        self.j = 0;

    def start_game(self):
        print ("Welcome to Tic Tac Toe! \n\nHere's the current board:");
        self.show_current_board();
        self.play();

    # Gets the value the player input
    def play(self):
        player_input_coordinates = self.get_player_input();
        while player_input_coordinates != PLAYER_QUIT: # Check that the player doesn't want to quit

            # Checks that the player entered a valid value
            isValid = self.player_input_is_valid(player_input_coordinates);
            if (isValid):

                if self.board.has_someone_placed_here(self.i, self.j): # Checks that no one has already placed there
                    self.board.set_player_move(self.player.get_player_move(), self.i, self.j);
                    self.show_current_board();
                    self.finish_game_if_end();
                    self.player.switch_player();
                else:
                    print (ERROR_MESSAGES[1]);
            else:
                print (ERROR_MESSAGES[0]);

            player_input_coordinates = self.get_player_input();

        exit(); # exit if the player wants to quit

    # Prints the current board to console
    def show_current_board(self):
        print(self.board.get_current_board_string());

    # Checks if the player entered a "<int>,<int>" for the coordinates in this format
    def player_input_is_valid(self, input_value):
        if len(input_value) == 3:
            if (input_value[1] == COMMA and str(input_value[0]).isdigit() and str(input_value[2]).isdigit()):
                x = int(input_value[0]);
                y = int(input_value[2]);
                if (x <= 3 and x >= 1 and y <= 3 and y >= 1):
                    self.i = y - 1;
                    self.j = x - 1;
                    return True;
        return False;

    def get_player_input(self):
        return input("Player " + str(self.player.get_player_number()) + " enter a coord x,y to place your " + self.player.get_player_move() + " or enter 'q' to give up: ");

    def finish_game_if_end(self):
        if self.board.won_the_game():
            print("\nCongratulations Player " + str(self.player.get_player_number()) + ", you won!!\n");
            exit();

        if self.board.last_move():
            print("Game over - It's a draw!\n");
            exit();
