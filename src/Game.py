from __future__ import annotations
from typing import *
from src.Player import Player
import pygame


class Game:
    """
    This class represents a game of ShootyBoats.

    === Public Attributes ===
    player1:
        The player that goes first; is a human player.
    player2:
        The player that goes second; is a CPU player.
    winner:
        The winner of the game, none if there are no winners yet.
    turn:
        The player who's turn it is.
    running:
        Whether this game is in progress or not.
    """
    player1: Player
    player2: Player
    winner: Optional[Player]
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
        self.running = False  # set the game to "off"

    def get_shot_coordinates(self) -> tuple:
        """
        Have the player who's turn it is make a "shoot" move. Return True if the
        move was made, False otherwise.
        """
        if self.turn is self.player1:
            return self.player1.ask_for_coordinates()
        return self.player2.get_random_coordinates()


    def place(self) -> bool:
        """
        Have the player who's turn it is, make a "place_ship" move. Return True
        if the ship was placed, False otherwise.
        """
        # TODO

    def is_game_over(self) -> bool:
        """
        Return True is game is over, false otherwise.
        """
        if self.player1.enemy_ships_sunk == 5 or \
                self.player2.enemy_ships_sunk == 5:
            self.end_game()
            return True
        else:
            return False

    def run_ship_placing_stage(self) -> None:
        """
        This runs the 1st stage of the game where both players place their ships
        on their ship board.
        """
        # TODO

    def battle_stage(self) -> None:
        """
        This runs the 2nd stage of the game where both players battle each
        other's boats.
        """
        # TODO

    def run_game(self) -> None:
        """
        Runs this game of ShootyBoats.
        """
        self.run_ship_placing_stage()
        self.run_battle_stage


    def end_game(self) -> None:
        """
        Ends this game of ShootyBoats.
        """
        self.running = False

    def get_move(self) -> tuple:
        """
        Get a move from the human player.
        """
        self.player1.getmove()

