from __future__ import annotations
from typing import List, Tuple, Optional


from src import Board

CARRIER, C = 5, "C"
BATTLESHIP, B = 4, "B"
DESTROYER, D = 3, "D"
SUBMARINE, S = 3, "S"
PATROL_BOAT, P = 2, "P"

DIMENSION = 10


class PlayerAbstract:
    """
    Capture a player for Sea Battle game. To be used with Game class for
    ShootyBoats. This is an abstract class, not to be instantiated directly.

    === Attributes ===
    name:
        Name for this player
    board:
        The CPUPlayer's PlayerBoard
    enemy_ships_sunk:
        Number of other player's ships sunk. Used to
        determine the winner of the game.

    === Representation Invariants ===
    -enemy_ships_sunk <= 5

    """
    name: str
    board: Board
    enemy_ships_sunk: int

    def __init__(self, name: str, board: Board) -> None:
        self.name = name
        self.board = board
        self.enemy_ships_sunk = 0

    def place_ship(self):
        pass

    def select_target(self):
        pass

    # TODO: Create more abstract methods as needed
