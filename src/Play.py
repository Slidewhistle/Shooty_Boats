from src.Game import *
from src.Board import *

if __name__ == "__main__":
    p1_board = Board()
    p2_board = Board()
    p1 = Player(p1_board)
    p2 = Player(p2_board)
    ShootyBoats = Game(p1, p2)
    ShootyBoats.run_game()
