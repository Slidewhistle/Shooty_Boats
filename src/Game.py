from __future__ import annotations
from src.Player import Player


class Game:
    """
    This class represents a game of ShootyBoats.

    === Public Attributes ===
    player1:
        The player that goes first; is a human player.
    player2:
        The player that goes second; is a CPU player.
    turn:
        The player who's turn it is.
    running:
        Whether this game is in progress or not.
    """
    player1: Player
    player2: Player
    turn: Player
    running: bool

    def __init__(self, player1: Player, player2: Player) -> None:
        """
        Initializes a game of ShootyBoats.
        """
        self.player1 = player1
        self.player2 = player2
        self.winner = None  # no winners when initialized
        self.turn = player1  # player1 starts off the game, so they get 1st turn

    def get_shot_coordinates(self) -> tuple:
        """
        Have the player who's turn it is make a "shoot" move. Return True if the
        move was made, False otherwise.
        """
        if self.turn is self.player1:
            return self.player1.select_target()
        return self.player2.get_random_coordinates()

    def run_ship_placing_stage(self) -> None:
        """
        Have the player who's turn it is, make a "place_ship" move. Return True
        if the ship was placed, False otherwise.
        """
        self.player1.place_ships()
        self.player2.place_ships_randomly()

    def run_battle_stage(self) -> None:
        """
        This runs the 2nd stage of the game where both players battle each
        other's boats.
        """
        while self.player1.enemy_ships_sunk != 5 or \
                self.player1.enemy_ships_sunk != 5:

            # have the human make a move and print the boards so human can see
            if self.turn is self.player1:
                print(self.player1.board.get_player_board_string())
                print(self.player2.board.get_target_board_string())
                self.player1.make_move()

            # if its not player1's move, have the random player move
            self.player2.make_random_move()

        # print winner
        if self.player1.enemy_ships_sunk == 5:
            print("Player1 has won")
        else:
            print("Player2 has won")

    def run_game(self) -> None:
        """
        Runs this game of ShootyBoats.
        """
        self.run_ship_placing_stage()
        self.run_battle_stage()



