from __future__ import annotations
from typing import List, Tuple, Optional

class Ships:
	"""
	Class used to represent the ships for a seabattle game.

	=== Attributes ===
	name:
		name of the ship
	size:
		length of the ship
	hits_left:
		number of hits a ship can currently sustain
	coords_A:
		list of coordinates the ship occupies that HAVE NOT been hit yet
	coords_D:
		list of coordinates the ship occupies that HAVE been hit
	is_sunk:	
		whether the ship is afloat(False) or sunk(True)

	=== Represenation Invariants ===
	- 2 <= size <= 5
	- name is either B, D, C, S, or P
	- the coordinates for the ship are strictly horizontal or vertical 
	
	"""
	name: str
	size: int
	hits_left: int
	coords_A: List[Tuple]
	coords_D: List[Tuple]
	is_sunk: bool

	def __init__(self, name: str, coords: List[Tuple]) -> None:
		"""
		Initializer for a ship object with name <name> and location <coords>
		"""
		self.name = name
		self.size, self.hits_left = len(coords)
		self.is_sunk = False
		self.coords_A = coords
		self.coords_D = []
	
	def hit(self, coord: Tuple) -> None:
		"""
		Records the hit at location <coord> for a ship object
		
		Precondition: <coord> is a valid coordinate to hit for this ship object
		"""
		self.coords_A.remove(coord)
		self.coords_B.append(coord)
		self.hits_left -= 1
		if self.hits_left == 0:
			self.is_sunk = True

		


