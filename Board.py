class Board:

    def __init__(self, board_ID):
        self.board = ['-' for i in range(9)]
        self.board_ID = board_ID
        self.game_state = 'Play'

    def get_board(self):
        board = '\r\n'
        for i in range(0,9,3):
            board += f"{self.board[i]}|{self.board[i+1]}|{self.board[i+2]}\r\n"
        return board

    def get_game_state(self):
        return self.game_state

    def print_board(self):
        for i in range(0,9,3):
            print(f"{self.board[i]}|{self.board[i+1]}|{self.board[i+2]}")
        return

    def mark_spot(self, position, mark):
        self.board[position] = mark
        return

    def is_full(self):
        for i in self.board:
            if i == '-':
                return False
        return True
