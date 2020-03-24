import tictactoe
import sys
import os

if __name__ == "__main__":
    if sys.platform == "win32":
        def win_clear():
            os.system("cls")
    elif sys.platform == "linux":
        def win_clear():
            os.system("clear")
    win_clear()
    board = tictactoe.Board(3)
    board.print_board()
    num = 1
    sign = input("Set player 1 sign: ")
    player1 = tictactoe.Player(sign, num)
    num += 2
    sign = input("Set player 2 sign: ")
    player2 = tictactoe.Player(sign, num)
    i = 1
    while board.finished != True:
        if i%2 == 1:
            print("Player 1 move: ")
            player1.moveX = int(input("Pos X: "))
            player1.moveY = int(input("Pos Y: "))
            board.get_move(player1)
            win_clear()
            board.print_board()
            board.check(player1, player2)
        else:
            print("Player 2 move: ")
            player2.moveX = int(input("Pos X: "))
            player2.moveY = int(input("Pos Y: "))
            board.get_move(player2)
            win_clear()
            board.print_board()
            board.check(player1, player2)
        i += 1
