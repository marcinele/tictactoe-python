import config
import random

class Board:
    size = 3
    board = []
    finished = True
    free_moves = []
    def __init__(self,_size):
        self.size = _size
        self.board = [[" " for x in range(4*self.size+1)] for y in range(2*self.size+1)]
        self.build_board()
        self.finished = False
        for x in range(1,_size+1):
            for y in range(1,_size+1):
                self.free_moves.append([x,y])

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
        self.free_moves.remove([player.moveX,player.moveY])

    def check(self, player1, player2): #only for 3x3 board
        temp_list_x = []
        temp_list_y = []
        for i in range(2,4*self.size-1,4):
            for j in range(1, 2*self.size+1, 2):
                temp_list_y.append(self.board[j][i])
            if self.check_of_check(temp_list_y, player1, player2) == None:
                return
            temp_list_y = []
        for i in range(1, 2*self.size+1, 2):
            for j in range(2,4*self.size-1,4):
                temp_list_x.append(self.board[i][j])
            if self.check_of_check(temp_list_x, player1, player2) == None:
                return
            temp_list_x = []
        temp_list_y.append(self.board[1][2])
        temp_list_y.append(self.board[3][6])
        temp_list_y.append(self.board[5][10])
        if self.check_of_check(temp_list_y, player1, player2) == None:
            return
        temp_list_x.append(self.board[1][10])
        temp_list_x.append(self.board[3][6])
        temp_list_x.append(self.board[5][2])
        if self.check_of_check(temp_list_x, player1, player2) == None:
            return
        temp_list_x = []
        if self.free_moves == []:
            config.window_refresh(self)
            print("Draw...")
            self.finished = True
            return

    def check_of_check(self, temp_list, player1, player2):
        if temp_list.count(player1.sign) == len(temp_list):
            config.window_refresh(self)
            print("Game over. Player ", player1.number, " (", player1.sign, ") won.")
            self.finished = True
            return None
        elif temp_list.count(player2.sign) == len(temp_list):
            config.window_refresh(self)
            print("Game over. Player ", player2.number, " (", player2.sign, ") won.")
            self.finished = True
            return None
        temp_list = []
        return 1




class Player:
    number = 0
    sign = "X"
    moveX = 0
    moveY = 0
    bot = False
    def __init__(self, _sign, _number, _bot):
        self.sign = _sign
        self.moveX = 999
        self.moveY = 999
        self.number = _number
        self.bot = _bot

    def move(self, board,players):
        if self.bot == False:
            print("Player",self.number,"(",self.sign,")","move")
            self.moveX = int(input("Cord X: "))
            self.moveY = int(input("Cord Y: "))
            board.get_move(self)
            board.check(players[0], players[1])
        else:
            ran_num = random.randint(0,len(board.free_moves)-1)
            moves = board.free_moves[ran_num]
            self.moveX = moves[0]
            self.moveY = moves[1]
            board.get_move(self)
            board.check(players[0], players[1])
