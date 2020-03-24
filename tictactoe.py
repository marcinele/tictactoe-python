class Board:
    size = 3
    board = []
    finished = True
    def __init__(self,_size):
        self.size = _size
        self.board = [[" " for x in range(4*self.size+1)] for y in range(2*self.size+1)]
        self.build_board()
        self.finished = False

    def build_board(self):
        x = 4*self.size+1
        y = 2*self.size+1
        for i in range(0,x):
            if i%4 == 0  :
                for j in range(1,y-1):
                    self.board[j][i] = "|"
        for i in range(0,y,2):
            for j in range(0,x):
                self.board[i][j] = "-"

    def print_board(self):
        for x in self.board:
            for y in x:
                print(y, end="")
            print("")

    def get_move(self, player):
        self.board[2*player.moveY-1][4*player.moveX-2] = player.sign

    def check(self, player1, player2): #only for 3x3 board
        temp_list_x = []
        temp_list_y = []
        for i in range(2,4*self.size-1,4):
            for j in range(1, 2*self.size+1, 2):
                temp_list_y.append(self.board[j][i])
            self.check_of_check(temp_list_y, player1, player2)
            temp_list_y = []
        for i in range(1, 2*self.size+1, 2):
            for j in range(2,4*self.size-1,4):
                temp_list_x.append(self.board[i][j])
            self.check_of_check(temp_list_x, player1, player2)
            temp_list_x = []
        for i in range(2,4*self.size-1,4):
            for j in range(1, 2*self.size+1, 2):
                temp_list_y.append(self.board[j][i])
            self.check_of_check(temp_list_y, player1, player2)
            temp_list_y = []
        temp_list_x.append(self.board[1][10])
        temp_list_x.append(self.board[3][6])
        temp_list_x.append(self.board[5][2])
        self.check_of_check(temp_list_x, player1, player2)
        temp_list_x = []

    def check_of_check(self, temp_list, player1, player2):
        if temp_list.count(player1.sign) == len(temp_list):
            print("Game over. Player ", player1.number, " (", player1.sign, ") won.")
            self.finished = True
        elif temp_list.count(player2.sign) == len(temp_list):
            print("Game over. Player ", player2.number, " (", player2.sign, ") won.")
            self.finished = True
        temp_list = []




class Player:
    number = 0
    sign = "X"
    moveX = 0
    moveY = 0
    def __init__(self, _sign, _number):
        self.sign = _sign
        moveX = 999
        moveY = 999
        number = _number
