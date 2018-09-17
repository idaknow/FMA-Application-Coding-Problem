#!/usr/bin/python
import sys

EMPTY_SPACE="."

class Board:

    def __init__(self):
        self.board = [[EMPTY_SPACE for x in range(3)] for y in range(3)]

    # Prints the current board to console
    def get_current_board_string(self):
        output_board = '\n';
        for j in self.board:
            for i in j:
                output_board += i + ' ';
            output_board += '\n\n';
        return output_board;

    def add_player_move(self, move, i, j):
        self.board[i][j] = move;

    def won_the_game(self):
        return self.row_win() or self.column_win() or self.diagonal_win();

    def row_win(self):
        for row in self.board:
            if (row[0] == row[1] == row[2]) and (row[0] != EMPTY_SPACE):
                return True;
        return False;

    def column_win(self):
        for column in range(0, 2):
            if (self.board[0][column] == self.board[1][column] == self.board[2][column]) and (self.board[0][column] != EMPTY_SPACE):
                return True;
        return False;

    def diagonal_win(self):
        if (self.board[0][0] == self.board[1][1] == self.board[2][2]) and (self.board[1][1] != EMPTY_SPACE):
            return True;
        if (self.board[0][2] == self.board[1][1] == self.board[2][0]) and (self.board[1][1] != EMPTY_SPACE):
            return True;
        return False;

    def last_move(self):
        for i in range(0,3):
            for j in range(0,3):
                if self.board[i][j] == EMPTY_SPACE:
                    return False;
        return True;
