import tictactoe



if __name__ == "__main__":
    board = tictactoe.Board(4)
    board.print_board()
    player1 = tictactoe.Player("X")
    player1.moveX = 4
    player1.moveY = 2
    board.get_move(player1)
    board.print_board()
