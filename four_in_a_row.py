from tkinter import *
from ex12.gui import *
from ex12.game import *
from ex12.excpetions import *
import time


def loop(gui):
    """ this function handles the use of the AI and checks for a win,
    and it uses an inner loop """
    gui.board_canvas.bind('<Button-1>', gui.click_and_play)
    cur_player = gui.game.get_current_player_object()
    if cur_player.get_mode() == AUTO:
        time.sleep(0.5)
        try:
            gui.click_and_play(0)

        except Winning_exception:
            pass
        except Illegal_move:
            pass

    if gui.game.get_game_over() is True:
        end_game_menu(gui)
        return

    gui.root.after(200, lambda gui=gui: loop(gui))


def end_game_menu(gui):
    """ a menu that appears when a game is over """
    gui.new_game_button = Button(gui.turn_manager, text='play again!',
                                 command=lambda new_game=gui: start_new_game(
                                     gui))
    gui.new_game_button.place(relx=0.5,rely=0.7,anchor=CENTER)
    gui.exit_game_button = Button(gui.turn_manager, text='exit game!',
                                  command=lambda exit=gui: exit_game(gui))
    gui.exit_game_button.place(relx=0.5,rely=0.9,anchor=CENTER)


def start_new_game(gui):
    """ handles the option in which the user chose to start a new game"""
    gui.board_canvas.destroy()
    gui.root.destroy()
    new_game = Game()
    root = Tk()
    new_gui = Gui(root, new_game)
    loop(new_gui)


def exit_game(gui):
    """ exits the game """
    gui.root.destroy()


if __name__ == '__main__':
    game = Game()
    root = Tk()
    gui = Gui(root, game)
    loop(gui)
    root.mainloop()
