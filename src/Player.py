from PlayerAbstract import *
from Ships import *
from board import *

CARRIER, C = 5, "C"
BATTLESHIP, B = 4, "B"
DESTROYER, D = 3, "D"
SUBMARINE, S = 3, "S"
PATROL_BOAT, P = 2, "P"

DIMENSION = 10


class Player(PlayerAbstract):
    def __init__(self, board: Board):
        """
        Initializes a Player in ShootyBoats
        """
        self.board = board
        self.enemy_ships_sunk = 0

    def ask_for_coordinates(self) -> tuple:
        """
        Asks the human player for coordinates
        """
        x = input("Enter")

    def place_ship(self, ship: Ships):
        for t in ship.coords_A:
            x = t[0]
            y = t[1]

            self.board.put_boat(x, y)

        # TODO: create five ships class into self.ship list

    # Overriding PlayerAbstract's select_target method.
    def select_target(self, x, y):
        self.board.give_boomed(x, y)

    def get_hit(self, x, y):
        for ship in self.ships:
            for coord in ship.coords_A:
                if coord[0] == x and coord[1] == y:
                    ship.hit(x,y)
                    if ship.is_sunk is True:
                        self.enemy_ships_sunk += 1

    def take_hit(self, x, y):
        self.shoot = True
        self.board.give_boomed(x, y)

    def change_turns_player(self):
        self.shoot = False


