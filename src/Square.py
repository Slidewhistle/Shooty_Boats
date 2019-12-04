class Square:
    """
        This class represents the board in the game.

        === Public Attributes ===
        x:
            x coordinate
        y:
            y coordinate
        boats:
            if there is a boat on it
        booms:
            if there is a broken boat on it
        """
    x: int
    y: int
    boats: bool
    boomed: bool

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.boats = False
        self.boomed = False

    def give_boomed(self):
        """
        hit the square
        """
        self.boomed = True

    def get_position(self):
        """
        get the position of the Square
        """
        return self.x, self.y

    def put_boat(self):
        """
        Put board on the square
        """
        self.boats = True

    def get_status(self):
        """
        Get the status of the square
        """
        if self.boats:
            if self.boomed:
                return "boomed boat"
            else:
                return "unboomed boat"
        else:
            if self.boomed:
                return "boomed nothing"
            else:
                return "nothing"

    def to_string(self):
        """
        returns a string representation of a square
        """
        if self.boats:
            if self.boomed:
                return "X"
            else:
                return "O"
        else:
            return " "



