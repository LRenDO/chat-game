# Socket Chat Project - Chat Game Class
# Class: CS372 Introduction to Computer Networks
# Author: Ren Demeis-Ortiz
# Description: This is a chat based tic tac toe game.

class ChatGame:
    PLAY = 'Play'
    X_WINS = 'x Wins!'
    O_WINS = 'o Wins!'
    DRAW = "It's a Draw."
    INSTRUCTIONS = "Welcome to Tic-Tac-Toe!" \
                   "\r\nYou can place a mark on a position by entering the " \
                        "number for the desired position (see below)\r\n" \
                        "1|2|3\r\n4|5|6\r\n7|8|9"

    def __init__(self):
        self.board = b.Board(1)
        px = px
        po = po

    def __valid_input(self, pos):
        pos = pos.split()
        position = []
        try:
            for p in pos:
                position.append(int(p))
        except(ValueError):
            position = None

        return position

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

    def set_px(self, player):
        self.px = player

    def set_po(self, player):
        self.po = player

    def get_px(self):
        return px

    def get_po(self):
        return po

    def still_playing(self):
        return self.board.get_game_state() == self.PLAY

    def update_board_state(self):
        self.__check_for_win(self.board)
        if self.still_playing() and self.boards[i].isFull():
            board.game_state = self.DRAW
        return

    def turn(self, player, position):
        position = self.__valid_input(position)
        if not position:
            return False

        else:
            # Mark spot
            self.board[position[0]][position[1]].mark_spot(player)

            # Update Status
            self.update_board_state()

            # If not still playing go through end sequences and break
            if self.board.get_game_state() != self.PLAY:
                return self.end_game()

            else:

                return self.board.get_board()

    def end_game(self):
        last_words = self.board.get_board()
        if self.board.get_game_state() == self.X_WINS:
            return last_words + self.X_WINS
        elif self.board.get_game_state() == self.O_WINS:
            return last_words + self.O_WINS
        elif self.board.get_game_state() == self.DRAW:
            return last_words += self.DRAW
