from src.Square import *

class Board:
    """
        This class represents the board in the game.

        === Public Attributes ===
        rows:
            the number of the rows in the board
        columns:
            the number of the column in the board
        width:
            The width of the board
        height:
            The height of the board
        startx:
            The left-up point's x coordinate
        starty:
            The left-up point's y coordinate
        dic:
            The 2D dictionary of the Squares
        chose:
            The square player now selected
    """
    ship_location: list
    board: list
    chose: (int, int)

    def __init__(self):

        self.board = []
        for x in range(7):
            self.board.append([])
            for y in range(7):
                self.board[x].append(Square(x, y))
        self.chose = (0, 0)

    def get_square(self, x, y):
        """
        To got a square inside the board
        """
        return self.board[x][y]



    def register_hit(self, x, y):
        """
        Hit the square.
        """
        self.get_square(x, y).give_boomed()

    def put_boat(self, x, y):
        """
        Put board on the square.
        """
        self.get_square(x, y).put_boat()

    def get_chose(self):
        """
        Returns the square last selected.
        """
        return self.chose

    def get_player_board_string(self):
        """
        Returns string representation of board.
        """
        s = ""
        s += "  "
        for col in range(7):
            s += str(col) + " "

        s += '\n'

        s += " +"
        for col in range(7):
            s += "-+"

        s += '\n'

        for row in range(7):
            s += str(row) + "|"
            for col in range(7):
                s += self.board[row][col].to_string() + "|"

            s += str(row) + "\n"

            s += " +"
            for col in range(7):
                s += "-+"
            s += '\n'

        s += "  "
        for col in range(7):
            s += str(col) + " "
        s += '\n'
        return s

    def get_target_board_string(self):
        """
        Returns string representation of enemies board.
        """
        s = ""
        s += "  "
        for col in range(7):
            s += str(col) + " "

        s += '\n'

        s += " +"
        for col in range(7):
            s += "-+"

        s += '\n'

        for row in range(7):
            s += str(row) + "|"
            for col in range(7):
                if self.board[row][col].to_string() != "O":
                    s += self.board[row][col].to_string() + "|"
                else:
                    s += " |"

            s += str(row) + "\n"

            s += " +"
            for col in range(7):
                s += "-+"
            s += '\n'

        s += "  "
        for col in range(7):
            s += str(col) + " "
        s += '\n'
        return s




