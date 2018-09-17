#!/usr/bin/python
import sys

from board import Board;
from player import Player;

# Welcome to Ida's TicTacToe!

WELCOME_MESSAGE = "Welcome to Tic Tac Toe! \n\nHere's the current board:"
ERROR_MESSAGE = {"General":"\nSorry, we could not recognise your input. Please try again.\n",
                "Duplicate":"\nSomeone is already placed here! Please enter another position.\n",
                "Invalid Numbers":"\nInvalid input numbers, make sure your co-ordinates are between 1,1 and 3,3. Try again!\n",
                "Incorrect Format":"\nSorry, we could not recognise your input. Make sure you're entering an \'x,y\', where X and Y are values between 1 and 3. Try again!\n"}
GAME_OVER_MESSAGE = "Game over - It\'s a draw!\n"
QUIT_GAME_MESSAGE = "\nYou quit the game - Goodbye!\n"
COMMA=","
QUIT="q"

class TicTacToe:

    # Initialises the tictactoe board, players and index values
    def __init__(self):
        self.board = Board();
        self.player = Player();
        self.i = 0; # indexes of the players coordinates
        self.j = 0;

    def start_game(self):
        print (WELCOME_MESSAGE);
        self.show_current_board();
        self.play();

    # loops through the game getting the player coordinates each time and checking that its valid
    def play(self):
        player_input_coordinates = self.get_player_input();
        while player_input_coordinates != QUIT:

            is_valid, error_message = self.player_input_is_valid(player_input_coordinates);
            if (is_valid):

                if self.board.has_someone_placed_here(self.i, self.j):
                    self.board.add_move_to_board(self.player.get_player_move(), self.i, self.j);
                    self.finish_game_if_end();
                    self.player.switch_player();
                else:
                    print (ERROR_MESSAGE["Duplicate"]);
            else:
                print (error_message);

            player_input_coordinates = self.get_player_input();

        print (QUIT_GAME_MESSAGE)
        exit(); # exit if the player wants to quit

    def show_current_board(self):
        print(self.board.get_current_board_string());

    # Checks if the player entered a "<int>,<int>" for the coordinates in this format
    # Returns a specific error message for invalid input
    def player_input_is_valid(self, input_value):
        error_message = '';
        is_valid = False;

        if len(input_value) == 3:
            if (input_value[1] == COMMA and str(input_value[0]).isdigit() and str(input_value[2]).isdigit()):
                x = int(input_value[0]);
                y = int(input_value[2]);
                if (x <= 3 and x >= 1 and y <= 3 and y >= 1):
                    # set the indexes of the co-ordinate position
                    self.i = y - 1;
                    self.j = x - 1;
                    is_valid = True;
                else:
                    error_message = ERROR_MESSAGE["Invalid Numbers"];
            else:
                error_message = ERROR_MESSAGE["Incorrect Format"];
        else:
            error_message = ERROR_MESSAGE["General"];
        return False, error_message;

    def get_player_input(self):
        return input("Player " + str(self.player.get_player_number()) + " enter a coord \'x,y\' to place your " + self.player.get_player_move() + " or enter \'q\' to give up: ");

    def finish_game_if_end(self):
        if self.board.won_the_game():
            print("\nCongratulations Player " + str(self.player.get_player_number()) + ", you won!!\n");
            exit();

        if self.board.last_move():
            print(GAME_OVER_MESSAGE);
            exit();
