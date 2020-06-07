from .disc import Disc

BOARD_HEIGHT = 6
BOARD_WIDTH = 7
EMPTY = '_'
BLUE = 'blue'
RED = 'red'
PLAYER_ONE = '1'
PLAYER_TWO = '2'


class Board:
    """ creates a board object """
    def __init__(self):
        self.__board = [['_', '_', '_', '_', '_', '_', '_'],
                      ['_', '_', '_', '_', '_', '_', '_'],
                      ['_', '_', '_', '_', '_', '_', '_'],
                      ['_', '_', '_', '_', '_', '_', '_'],
                      ['_', '_', '_', '_', '_', '_', '_'],
                      ['_', '_', '_', '_', '_', '_', '_']]

        self.__discs = []

    def get_board(self):
        """ returns thhe current state of the board """
        return self.__board

    def get_player_at(self, row, col):
        """ returns the player at the (row, col) coordinate """
        if self.__board[row][col] == BLUE:
            return PLAYER_ONE
        elif self.__board[row][col] == RED:
            return PLAYER_TWO
        else:
            return None

    def get_discs_list(self):
        """ returns the discs list """
        return self.__discs

    def update_discs_list(self, disc):
        """ adds a disc to the discs list """
        self.__discs.append(disc)

    def update_board(self, x_location, y_location, color):
        self.__board[x_location][y_location] = color

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        board_str = ''
        for row in range(BOARD_HEIGHT):
            row_str = ''
            for col in range(BOARD_WIDTH):
                row_str += self.__board[row][col] + " "
            board_str += row_str + "\n"
        return board_str
     
    def add_disc(self, disc, column):
        """ adds a disc to the board """
        if self.is_legal(column):
            x, y = self.is_legal(column)
            disc.set_location((x,y))
            self.update_board(x, y, disc.get_color())
            self.update_discs_list(disc)
            return True
        else:
            return None

    def possible_moves(self):
        """ returns a list of all possible moves """
        possible_moves_list=[]
        for col in range(BOARD_WIDTH):
            if self.is_legal(col):
                possible_moves_list.append(self.is_legal(col))
        return possible_moves_list

    def is_legal(self, column):
        """ checks if it's legal to insert a disc to in a given column. """
        row = None
        if column not in range(BOARD_WIDTH):
            return False
        for i in range(BOARD_HEIGHT-1,-1,-1):
            if self.__board[i][column] == EMPTY:
                row = i
                break
        if row is None:
            return False
        else:
            return (row,column)

    def cell_content(self, coordinate):
        """ return the disc a given location """
        x_location,y_location = coordinate
        return self.__board[x_location][y_location]



    



