from __future__ import annotations
from typing import List, Tuple, Optional
from random import randint

CARRIER, C = 5, "C"
BATTLESHIP, B = 4, "B"
DESTROYER, D = 3, "D"
SUBMARINE, S = 3, "S"
PATROL_BOAT, P = 2, "P"

DIMENSION = 10


class CPUPlayer(PlayerAbstract):
    """
    Capture an AI player for Sea Battle game.
    To be used with Game class for ShootyBoats

    === Attributes ===
    seen_squares:
        Coordinates of Squares on the
        TargetBoard of board that have been interacted with.
    successful_hits:
        Coordinates of TargetBoard known to contain an enemy ship
    ship_squares:
        Coordinates of Squares on the
        ShipBoard that have been interacted with.
    === Representation Invariants ===
    -enemy_ships_sunk <= 5

    """
    name: str
    board: PlayerBoard
    enemy_ships_sunk: int
    seen_squares: List[Tuple]
    successful_hits: List[Tuple]
    ship_squares: List[Tuple]

    def __init__(self, name: str, board: PlayerBoard) -> None:
        """
        Initialize this CPUPlayer
        """
        PlayerAbstract.__init__(self, name, board)
        self.seen_squares = []
        self.ship_squares = []

    def place_ships(self):
        """
        Place ships on ShipBoard of self.board.
        Use _place_ship method
        Order of ship placement is:
        Carrier->Battleship->Submarine->Destroyer->Patrol boat

        Randomly choose a row and column, as well as an orientation.
        """
        self._place_ship(CARRIER, C)
        self._place_ship(BATTLESHIP, B)
        self._place_ship(DESTROYER, D)
        self._place_ship(SUBMARINE, S)
        self._place_ship(PATROL_BOAT, P)

    def _place_ship(self, size: int, ship: str):
        """
        Place ship, in a row or column
        Do not overlap ships, use self.ship_squares to check
        """
        not_placed = True

        while not_placed:
            row = randint(0, DIMENSION - 1)  # Pick a row at random
            column = randint(0, DIMENSION - 1)  # Pick a column at random
            orientation = randint(0, 1)  # 0 for horizontal

            if orientation == 0:  # horizontal, place in a row
                if column > size:  # Corner cases (6, 7, 8, 9)
                    for i in range(size, column):
                        if (i, row) in self.ship_squares:
                            break
                        self.board.place_ship(ship, i, row)
                        self.ship_squares.append((i, row))
                        not_placed = False
                else:
                    count = 0
                    for i in range(column, column + size):
                        if (i, row) in self.ship_squares:
                            break
                        else:
                            self.board.place_ship(ship, i, row)
                            self.ship_squares.append((i, row))
                            count += 1
                    if count == size:
                        not_placed = False

            else:  # vertical, place in a column
                if row > size:  # Corner cases (6, 7, 8, 9)
                    if column != self.ship_squares[0][1]:
                        for i in range(size, row):
                            self.board.place_ship(ship, column, i)
                            self.ship_squares.append((column, i))
                            not_placed = False
                else:
                    count = 0
                    for i in range(row, row + size):
                        if (column, i) in self.ship_squares:
                            break
                        else:
                            self.board.place_ship(ship, column, i)
                            self.ship_squares.append((coumn, i))
                            count += 1
                    if count == size:
                        not_placed = False

    def select_target(self) -> Tuple:
        """
        Select a TargetBoard square to fire on.
        This is done randomly, until an enemy ship is successfully hit
        """
        if len(self.successful_hits) == 0:
            while True:
                row = randint(0, DIMENSION - 1)  # Pick a row at random
                column = randint(0, DIMENSION - 1)  # Pick a column at random
                if (column, row) not in self.seen_squares:
                    return column, row

        # TODO: Develop a guessing algorithm


    def update_successful_hits(self, ship: str) -> Tuple:
        """
        After an enemy ship is sunk, its coordinates are ignored
        for future selection choices.

        This is of course not guaranteed to ignore that specific ship,
        but it does make the AI guess more intelligently.

        Precondition: This method is called immediately after a
                      ship of type <ship> has been sunk
        """

        # TODO: Develop this algorithm

        pass
