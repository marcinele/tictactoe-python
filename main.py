import tictactoe
import config

if __name__ == "__main__":
    board = tictactoe.Board(3)
    config.window_refresh(board)
    players = []
    players = config.config_players()
    i = 0
    while board.finished != True:
        config.window_refresh(board)
        players[i%2].move(board,players)
        i += 1
