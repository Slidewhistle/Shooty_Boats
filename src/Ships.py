from __future__ import annotations
from typing import List, Tuple, Optional

class Ships:
	"""
	Class used to represent the ships for a seabattle game.

	=== Attributes ===
	name:
		name of the ship
	coords_A:
		where the ship is located
	is_sunk:	
		whether the ship is afloat(False) or sunk(True)

	=== Represenation Invariants ===
	- name is either B, D, C, S, or P
	- the coordinates for the ship are strictly horizontal or vertical 
	
	"""
	name: str
	coords_A: List[Tuple]
	is_sunk: bool

	def __init__(self, name: str, coords: List[Tuple]) -> None:
		"""
		Initializer for a ship object with name <name> and location <coords>
		"""
		self.name = name
		self.is_sunk = False
		self.coords_A = coords

	
	def hit(self, coord: Tuple) -> None:
		"""
		Records the hit at location <coord> for a ship object
		
		Precondition: <coord> is a valid coordinate to hit for this ship object
		"""
		self.is_sunk = True

		


