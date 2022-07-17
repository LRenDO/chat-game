# Socket Chat Project - Chat Mega Game Class
# Class: CS372 Introduction to Computer Networks
# Author: Ren Demeis-Ortiz
# Description: This is a chat based tic tac toe game.
#              except there are 9 boards and you must win
#              on 3 boards in a line.

class ChatGame:
    PLAY = 'Play'
    X_WINS = 'x Wins'
    O_WINS = 'o Wins'
    DRAW = "It's a Draw"

    def __init__(self, px, po):
        self.boards = [b.Board(1), b.Board(2), b.Board(3), b.Board(4),
                  b.Board(5), b.Board(6), b.Board(7),b.Board(8), b.Board(9)]
        self.main_board = b.Board()
        px = px
        po = po
        self.main_game_state = self.PLAY

    def print_boards(self):
        for board in self.boards:
            board.print_board()
        return

    def __check_for_win(self, board):
        # Potential lines that you must have one of to win
        lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],
                [2, 5, 8], [2, 4, 6], [0, 4, 8]]
        for l in lines:
            if board[0] == 'x' or board[0] == 'o':
                if board[l[0]] == board[l[1]] and board[l[1]] == board[l[2]]:
                    if board[l[0]] == 'x':
                        board.game_state = self.X_WINS
                    if board[l[0]] == 'o':
                        board.game_state = self.O_WINS
        return

    def update_board_statuses(self, board_nums):
        for i in board_nums:
            self.__check_for_win(self.boards[i])
            if boards[i].game_state == self.PLAY and self.boards[i].isFull():
                board.game_state = self.DRAW
        return

    def update_main_status(self):
        for i in range(9):
            game_state = self.boards[i].get_game_state()
            if game_state == self.X_WINS:
                self.main_board[i] = 'x'

            if game_state == self.O_WINS:
                self.main_board[i] = 'o'

            if game_state == self.DRAW:
                self.main_board[i] = 'd'

            self.__check_for_win(self.main_board)

            if self.main_board.game_state == self.PLAY and \
                    self.main_board.isFull():
                self.main_board.game_state = self.DRAW

    def turn(self, player, position):
        position = self.__valid_input(position)
        if not position:
            return False

        else:
            # Mark spot
            boards[position[0]][position[1]].mark_spot(player)
            # Update Status
            # Update and Check Status of Main Game
            #
            # If not still playing go through end sequences and break

            return True

    def __valid_input(self, pos):
        pos = pos.split()
        position = []
        try:
            for p in pos:
                position.append(int(p))
        except:
            position = None

        return position

    def still_playing(self):
        return self.game_state == self.PLAY
