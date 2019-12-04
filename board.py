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
    rows: int
    columns: int
    width: int
    height: int
    startx: int
    starty: int
    chose: (int, int)

    def __init__(self, rows, columns, width, height, startx=0, starty=0):
        self.rows = rows
        self.columns = columns
        self.width = width
        self.height = height
        self.startx = startx
        self.starty = starty
        self.square_width = int(width / rows)
        self.square_height = int(height / columns)
        self.dic = {}
        for x in range(self.columns):
            self.dic[x] = {}
            for y in range(self.rows):
                self.dic[x][y] = Square(self.square_width * x, self.square_height * y)
        self.chose = (0, 0)

    def get_square(self, x, y):
        """
        To got a square inside the board
        """
        return self.dic[x][y]

    def get_positionx(self, x, y):
        """
        To got a square's x position
        """

        return self.dic[x][y].get_position()[1]

    def get_positiony(self, x, y):
        """
        To got a square's y position
        """
        return self.dic[x][y].get_position()[0]

    def get_width(self):
        """
        Get the square width
        """
        return self.square_width - 3

    def get_height(self):
        """
        Get the square height
        """
        return self.square_height - 3

    def draw_it(self, x, y):
        """
        Get the information you need to draw the square
        """
        if not (x, y) == self.chose:
            return self.get_positionx(x, y), self.get_positiony(x, y), self.get_width(), self.get_width()
        else:
            return self.get_positionx(x, y), self.get_positiony(x, y), int(self.get_width() * 4 / 3), int(
                self.get_width() * 4 / 3)

    def go_left(self):
        """
        Move the chosen one square go left
        """
        a, b = self.chose
        if b != 0:
            self.chose = a, b - 1
        else:
            self.chose = a, self.rows - 1

    def go_right(self):
        """
        Move the chosen one square go right
        """
        a, b = self.chose
        if b != self.rows - 1:
            self.chose = a, b + 1
        else:
            self.chose = a, 0

    def go_up(self):
        """
        Move the chosen one square go up
        """
        a, b = self.chose
        if a != 0:
            self.chose = a - 1, b
        else:
            self.chose = self.columns - 1, b

    def go_down(self):
        """
        Move the chosen one square go down
        """
        a, b = self.chose
        if a != self.columns - 1:
            self.chose = a + 1, b
        else:
            self.chose = 0, b

    def get_color(self, x, y):
        """
        Get the color of the square
        """
        if (x, y) == self.chose:
            return 0, 0, 255
        square = self.get_square(x, y)
        if square.get_status() == "boomed boat":
            return 255, 0, 0
        if square.get_status() == "unboomed boat":
            return 255, 255, 0
        if square.get_status() == "boomed nothing":
            return 255, 0, 255
        if square.get_status() == "nothing":
            return 0, 255, 0

    def give_boomed(self, x, y):
        """
        Hit the square
        """
        self.get_square(x, y).give_boomed()

    def put_boat(self, x, y):
        """
        Put board on the square
        """
        self.get_square(x, y).put_boat()

    def get_chosen_one(self):
        """
        get the chosen one square
        """
        return self.chose


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
