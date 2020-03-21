class Board:
    size = 3
    board = []
    finished = True
    def __init__(self,_size):
        self.size = _size
        self.board = [[" " for x in range(4*self.size+1)] for y in range(self.size+2)]
        self.build_board()
        self.finished = False

    def build_board(self):
        x = 4*self.size+1
        y = self.size+2
        for i in range(0,x):
            self.board[0][i] = "-"
            self.board[y-1][i] = "-"
            if i%4 == 0  :
                for j in range(1,y-1):
                    self.board[j][i] = "|"

    def print_board(self):
        for x in self.board:
            for y in x:
                print(y, end="")
            print("")

    def get_move(self, player):
        self.board[player.moveY][4*player.moveX-2] = player.sign


class Player:
    sign = "X"
    moveX = 0
    moveY = 0
    def __init__(self, _sign):
        self.sign = _sign
        moveX = 999
        moveY = 999
