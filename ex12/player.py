
PLAYER_1 = '1'
PLAYER_2 = '2'
BLUE = 'blue'
RED = 'red'


class Player:
    def __init__(self,name,mode):
        '''
        :param name: 1 for player 1 and 2 for player 2
        :param mode: auto or manual player
        '''
        self.__name = name
        self.__mode = mode
        if self.__name == PLAYER_1:
            self.__color=BLUE
            self.__my_turn=True
        else:
            self.__color=RED
            self.__my_turn=False

    def get_name(self):
        '''
        :return: 1 for player 1 and 2 for player 2
        '''
        return self.__name

    def get_mode(self):
        '''
        :return: auto or manual
        '''
        return self.__mode

    def get_color(self):
        '''
        :return: blue or red
        '''
        return self.__color

    def get_my_turn(self):
        '''
        :return: True if it is the turn of the player and false otherwise
        '''
        return self.__my_turn

    def set_mode(self,game_mode):
        '''
        sets the game mode
        :param game_mode: auto or manual
        :return: None
        '''
        self.__mode=game_mode

    def set_my_turn(self,turn):
        '''
        sets the turn status.
        :param turn: True or False
        :return:None
        '''
        self.__my_turn=turn

