from .board import *
from .disc import *
from .player import *
from .excpetions import *

PLAYER_1 = '1'
PLAYER_2 = '2'
ERROR_MSG = 'Illegal location.'
ERROR_MSG_MOVE = 'Illegal move.'
BLUE = 'blue'
RED = 'red'
TIE=0
POSSIBLE_WINNERS=[int(PLAYER_1),int(PLAYER_2),TIE]
FULL_BOARD = 42
BOARD_HEIGHT = 6
BOARD_WIDTH = 7
CONNECT_FOUR = 4
EMPTY = '_'
CHOOSE_COLUMN_MSG = 'Please choose a column to insert a disc'
PLAYER_1_WIN_MSG = 'PLAYER 1 WIN!'
PLAYER_2_WIN_MSG = 'PLAYER 2 WIN!'
TIE_MSG = 'TIE'
AUTO = 'auto'
MANUAL = 'manual'


class Game:
    def __init__(self):
        """ builds a game object """
        self.__board = Board()
        self.__discs = self.__board.get_discs_list()
        self.player_1 = Player(PLAYER_1, None)
        self.player_2 = Player(PLAYER_2, None)
        self.win_list = []
        self.end_game_status=''
        self.game_over = False

    def get_game_over(self):
        """ :return: True if the game is finished or False otherwise """
        return self.game_over

    def set_game_over(self,value):
        """ sets game over state """
        self.game_over=value

    def get_win_list(self):
        """ :returns the win list """
        return self.win_list

    def get_end_game_status(self):
        """ :returns the end game status """
        return self.end_game_status

    def set_end_game_status(self,status):
        """ sets the end game status """
        self.end_game_status=status

    def get_discs_list(self):
        """ returns the discs list """
        return self.__discs

    def get_board(self):
        """ :returns the board """
        return self.__board.get_board()

    def change_turns(self):
        """ sets the current turn of the players """
        for player in self.get_players():
            if player.get_my_turn() is True:
                player.set_my_turn(False)
            else:
                player.set_my_turn(True)

    def get_players(self):
        """ returns a list of the players """
        return [self.player_1, self.player_2]

    def make_move(self, column):
        """ makes a move in the game """
        for player in self.get_players():
            if player.get_my_turn() is True:
                disc = Disc(player.get_color())
                if self.__board.is_legal(column) is False:
                    raise Exception(ERROR_MSG_MOVE)
                elif self.get_winner() in POSSIBLE_WINNERS:
                    raise Exception(ERROR_MSG_MOVE)

                elif len(self.__discs) == FULL_BOARD:
                    raise Exception(ERROR_MSG_MOVE)

                self.__board.add_disc(disc, column)
        self.change_turns()

    def get_winner(self):
        '''
        this function checks if the game ended by victory.
        :return: the winning color
        '''
        if len(self.__discs) == 0:
            return
        last_move = self.__discs[-1]
        color = last_move.get_color()
        row, column = last_move.get_location()
        counter = 0
        if self.check_rows(color, counter, row) or \
                self.check_columns(color, column, counter, row) or \
                self.check_diagonal_right(color, column, counter, row) or \
                self.check_diagonal_left(color, column, counter, row):
            if color==BLUE:
                status=PLAYER_1
            else:
                status=PLAYER_2
            self.set_end_game_status(status)
            return int(status)
        if len(self.__discs)==FULL_BOARD:
            self.win_list=[]
            self.set_end_game_status(TIE)
            return TIE
        return


    def check_diagonal_left(self, color, column, counter, row):
        '''
        checks for winner in a diagonal from down right to up left.
        :param color: color of the last move
        :param column: column of the last move
        :param counter: int
        :param row: row of the last move
        :return: True for victory, None otherwise
        '''
        self.win_list = []
        down_limit = min(BOARD_HEIGHT - 1 - row, BOARD_WIDTH - 1 - column)
        down_row, right_col = row + down_limit, column + down_limit
        up_limit = min(row, column)
        up_row, left_col = row - up_limit, column - up_limit
        i = down_row
        j = right_col
        while i >= up_row and j >= left_col:
            if self.__board.cell_content((i, j)) == color:
                counter += 1
                self.win_list.append((i, j))
            else:
                counter = 0
                self.win_list = []
            i -= 1
            j -= 1
            if counter == CONNECT_FOUR:
                return True

    def check_diagonal_right(self, color, column, counter, row):
        '''
        checks for winner in a diagonal from down left to up right.
        :param color: last move color
        :param column: last move column
        :param counter: int
        :param row: last move row
        :return: True for victory, None otherwise
        '''
        self.win_list = []
        down_limit = min(BOARD_HEIGHT - 1 - row, column)
        down_row, left_col = row + down_limit, column - down_limit
        up_limit = min(row, BOARD_WIDTH - 1 - column)
        up_row, right_col = row - up_limit, column + up_limit
        i = down_row
        j = left_col
        while i >= up_row and j <= right_col:
            if self.__board.cell_content((i, j)) == color:
                counter += 1
                self.win_list.append((i, j))
            else:
                counter = 0
                self.win_list = []
            i -= 1
            j += 1
            if counter == CONNECT_FOUR:
                return True

    def check_columns(self, color, column, counter, row):
        '''
        checks for winner in columns
        :param color: last move color
        :param column: last move column
        :param counter: int
        :param row: last move row
        :return: True for victory, None otherwise
        '''
        self.win_list = []
        for i in range(BOARD_HEIGHT - 1, row - 1, -1):
            if self.__board.cell_content((i, column)) == color:
                counter += 1
                self.win_list.append((i, column))
            else:
                counter = 0
                self.win_list = []

            if counter == CONNECT_FOUR:
                return True

    def check_rows(self, color, counter, row):
        '''
        checks for winner in rows
        :param color: last move color
        :param counter: int
        :param row: last move row
        :return: True for victory, None otherwise
        '''
        self.win_list = []
        for j in range(BOARD_WIDTH):
            if self.__board.cell_content((row, j)) == color:
                counter += 1
                self.win_list.append((row, j))
            else:
                counter = 0
                self.win_list = []
            if counter == CONNECT_FOUR:
                return True

    def get_player_at(self, row, col):
        """ returns the player at the given coordinate """
        try:
            player_at = self.__board.get_player_at(row, col)
            return int(player_at) if player_at is not None else player_at
        except:
            raise Exception(ERROR_MSG)

    def get_current_player(self):
        """ returns the player's name which has the turn """
        for player in self.get_players():
            if player.get_my_turn() is True:
                return int(player.get_name())

    def get_current_player_object(self):
        """ returns the player object which has the turn """
        for player in self.get_players():
            if player.get_my_turn() is True:
                return player
