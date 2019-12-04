from src.PlayerAbstract import *
from src.Board import *


class Player(PlayerAbstract):
    """
    This class represents the human player of ShootyBoats.

    === Public Attributes ===
    board:
        The board that this player is playing on.
    """
    def __init__(self, board: Board):
        """
        Initializes a Player in ShootyBoats
        """
        self.board = board
        self.enemy_ships_sunk = 0

    def ask_for_coordinates(self) -> tuple:
        """
        Asks the human player for coordinates.
        """
        print("Enter the coordinates where you want to place your ships:")
        x = input("Enter an x coordinate to:")
        y = input("Enter a y coordinate:")
        return x, y

    def place_ships(self):
        """
        Places all 5 ships on the board according to player's input.
        """
        for i in range(5):
            point = self.ask_for_coordinates()
            self.board.put_boat(point[0], point[1])

    def select_target(self):
        """
        Asks the human player for coordinates.
        """
        print("Enter the coordinates where you want to shoot:")
        x = input("Enter an x coordinate to:")
        y = input("Enter a y coordinate:")
        return x, y





