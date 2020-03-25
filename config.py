import sys
import os
import tictactoe

if sys.platform == "win32":
    def win_clear():
        os.system("cls")
elif sys.platform == "linux":
    def win_clear():
        os.system("clear")

def window_refresh(board):
    win_clear()
    board.print_board()

def config_players():
    players = []
    answ = input("Wanna play with bot? (yes/no): ")
    if answ == "yes":
        players.append(tictactoe.Player("X",1,False))
        players.append(tictactoe.Player("Y",2,True))
    elif answ == "no":
        players.append(tictactoe.Player("X",1,False))
        players.append(tictactoe.Player("Y",2,False))
    else:
        print("idk what to do")
    return players
