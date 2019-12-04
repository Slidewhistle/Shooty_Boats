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
        for x in range(10):
            self.board.append([])
            for y in range(10):
                self.board[x].append(Square(x, y))
        self.chose = (0, 0)

    def get_square(self, x, y):
        """
        To got a square inside the board
        """
        return self.dic[x][y]



    def register_hit(self, x, y):
        """
        Hit the square
        """
        self.get_square(x, y).give_boomed()

    def put_boat(self, x, y):
        """
        Put board on the square
        """
        self.get_square(x, y).put_boat()

    def get_chose(self):
        """
        returns the square last selected
        """
        return self.chose

    def to_string(self):
        """
        returns string representation of board
        """
        s = ""
        s += "  "
        for  col in range(10):
            s += str(col) + " "

        s += '\n'

        s += " +"
        for  col in range(10):
            s += "-+"

        s += '\n';

        for row in range(10):
            s += str(row) + "|"
            for col in range(10):
                s += self.board[row][col].to_string() + "|"

            s += str(row) + "\n"

            s += " +";
            for col in range(10):
                s += "-+";
            s += '\n';

        s += "  ";
        for col in range(10):
            s += str(col) + " "
        s += '\n';
        return s;



