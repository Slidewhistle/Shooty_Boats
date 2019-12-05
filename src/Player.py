from __future__ import annotations
from src.Board import *
from random import *



class Player:
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
        self.opponent = None

    def ask_for_coordinates(self) -> tuple:
        """
        Asks the human player for coordinates.
        """
        print("Enter the coordinates where you want to place your ships (values should be between 0 and 6 (inclusive)):")
        x = input("Enter an x coordinate:")
        y = input("Enter a y coordinate:")
        return x, y

    def get_random_coordinates(self) -> tuple:
        """
        Generates a random coordinate for the cpu player to place a ship or
        shoot a shot.
        """
        random_x = randint(0, 6)
        random_y = randint(0, 6)
        return random_x, random_y

    def place_ships(self):
        """
        Places all 5 ships on the board according to player's input.
        """
        for i in range(5):
            point = self.ask_for_coordinates()
            self.board.put_boat(int(point[0]), int(point[1]))

    def place_ships_randomly(self):
        """
        Places all 5 ships on the board randomly.
        """
        for i in range(5):
            point = self.get_random_coordinates()
            self.board.put_boat(int(point[0]), int(point[1]))

    def select_target(self) -> tuple:
        """
        Asks the human player for coordinates.
        """
        print("Enter the coordinates where you want to shoot:")
        x = input("Enter an x coordinate to:")
        y = input("Enter a y coordinate:")
        return x, y

    def add_opponent(self, opponent: Player):
        """
        Sets this player's opponent.
        """
        self.opponent = opponent

    def make_move(self):
        """
        Makes a move by consulting a human.
        """
        move = self.select_target()
        self.opponent.board.register_hit(int(move[0]), int(move[1]))

    def make_random_move(self):
        """
        Makes random move.
        """
        move = self.get_random_coordinates()
        self.opponent.board.register_hit(int(move[0]), int(move[1]))



