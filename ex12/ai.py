from .game import *
import random
AI_ERROR_MSG = 'No possible AI moves.'

class AI:
    def __init__(self, game, player):
        """ creates an AI object """
        self.game = game
        self.player = player

    def find_legal_move(self, timeout=None):
        """ finds a legal move for the AI """
        if self.game.get_winner() is not None:
            raise Illegal_move(AI_ERROR_MSG)

        num = random.randint(0, 6)
        while self.game.get_player_at(0, num) is not None:
            num = random.randint(0, 6)
        return num

    def get_last_found_move(self):
        pass
