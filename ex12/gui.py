from tkinter import *
from .game import *
from .player import *
from .ai import AI

ROOT_SIZE = '670x760'
OVAL_BIG_R = 95.71
OVAL_SMALL_R = 75
HEIGHT_LIMIT = 450
WIDTH_LIMIT = 670
BOARD_SIZE = 42
POSSIBLE_POINTER_POSITION = [47.855, 143.565, 239.275, 334.985, 430.695,
                             526.405, 622.115]
PLAYER_1_TURN_MSG='<<< YOUR TURN'
PLAYER_2_TURN_MSG='YOUR TURN >>>'
EMPTY_STR = ''

class Gui:

    def __init__(self, root, game):
        """ builds a gui object """
        self.game = game
        self.root = root
        self.root.geometry(ROOT_SIZE)
        self.root.resizable(False,False)

        self.init_labels()

        self.init_canvases()

        self.init_buttons()

        self.oval_list = self.create_board()

        self.init_packs()

    def init_packs(self):
        """ packs the title, main canvas, and the buttons"""
        self.title.pack()
        self.main_canvas.pack(expand=YES, fill=BOTH)
        self.auto_game.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.one_player.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.two_players.place(relx=0.5, rely=0.6, anchor=CENTER)
        self.pointer = self.board_canvas.create_line(0, 0, 0, 0, arrow=LAST,
                                                      fill='blue',width=10)

    def init_buttons(self):
        """ creates the buttons of the intro screen """
        self.one_player = Button(self.main_canvas, text='ONE PLAYER',
                                 command=lambda: [self.one_player_chosen()],
                                 font=50)
        self.two_players = Button(self.main_canvas, text='TWO PLAYERS',
                                  command=lambda: [self.two_players_chosen(),
                                                   self.prepare_board()],
                                  font=50)
        self.you_start = Button(self.main_canvas, text='YOU START',
                                command=lambda: [self.you_start_chosen(),
                                                 self.prepare_board()],
                                font=50)
        self.cpu_start = Button(self.main_canvas, text='COMPUTER START',
                                command=lambda: [self.cpu_start_chosen(),
                                                 self.prepare_board()],
                                font=50)
        self.auto_game = Button(self.main_canvas, text='AUTO MODE ',
                                command=lambda: [self.auto_mode_chosen(),
                                                 self.prepare_board()],
                                font=50)
        self.return_button = Button(self.main_canvas, text='RETURN',
                                    command=lambda: [self.return_chosen()])

    def init_canvases(self):
        """ creates the main canvas and the board canvas and their
         functionality"""
        self.main_canvas = Canvas(self.root, width=670, height=600)
        self.main_img = PhotoImage(file="ex12/4 in a row entering.png")
        self.main_canvas.create_image(0, 0, image=self.main_img, anchor=NW)
        self.board_canvas = Canvas(self.root, width=670, height=600,
                                   bg='saddle brown')
        self.board_canvas.bind('<Button-1>', self.click_and_play)
        self.board_canvas.bind('<Motion>', self.motion)

    def init_labels(self):
        """ creates the labels of the gui object """
        self.title_img = PhotoImage(file='ex12/title.png')
        self.title = Label(self.root, image=self.title_img, width=670,
                           height=160)
        self.turn_manager_img = PhotoImage(file='ex12/turn_manager_title.png')
        self.turn_manager = Canvas(self.root,width=670,height=190)
        self.turn_manager.create_image(0,0,image=self.turn_manager_img,
                                       anchor=NW)
        self.turn_message = Message(self.turn_manager, text=PLAYER_1_TURN_MSG,
                                    width=150, font=40)
        self.player_1_img=PhotoImage(file='ex12/gil_blue.png')
        self.player_1_title = Label(self.turn_manager, image=self.player_1_img,
                                    width=100, height=182,
                                    font=50)
        self.player_2_img=PhotoImage(file='ex12/yonatan_red.png')
        self.player_2_title = Label(self.turn_manager, image=self.player_2_img,
                                    width=100, height=182,
                                    font=50)
    def get_root(self):
        """ :returns the root of the gui object """
        return self.root

    def return_chosen(self):
        """ handles the return button"""
        self.auto_game.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.one_player.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.two_players.place(relx=0.5, rely=0.6, anchor=CENTER)
        self.you_start.place_forget()
        self.cpu_start.place_forget()
        self.return_button.place_forget()

    def cpu_start_chosen(self):
        """ handles the cpu_start button and creates an AI object
         accordingly"""
        self.you_start.place_forget()
        self.cpu_start.place_forget()
        self.return_button.place_forget()
        self.main_canvas.pack_forget()
        self.title.pack_forget()
        player_1, player_2 = self.game.get_players()[0], \
                             self.game.get_players()[1]
        player_1.set_mode(AUTO)
        self.ai_1 = AI(self.game, PLAYER_ONE)
        player_2.set_mode(MANUAL)

    def you_start_chosen(self):
        """ handles the you_start button and creates an AI object
        accordingly """
        self.you_start.place_forget()
        self.cpu_start.place_forget()
        self.return_button.place_forget()
        self.main_canvas.pack_forget()
        self.title.pack_forget()
        player_1, player_2 = self.game.get_players()[0], \
                             self.game.get_players()[1]
        player_1.set_mode(MANUAL)
        player_2.set_mode(AUTO)
        self.ai_2 = AI(self.game, PLAYER_TWO)

    def auto_mode_chosen(self):
        """ handles the auto_mode_chosen button and creates the AI objects
        accordingly """
        self.one_player.place_forget()
        self.auto_game.place_forget()
        self.two_players.place_forget()
        self.main_canvas.pack_forget()
        self.title.pack_forget()
        player_1, player_2 = self.game.get_players()[0], \
                             self.game.get_players()[1]
        player_1.set_mode(AUTO)
        player_2.set_mode(AUTO)
        self.ai_1 = AI(self.game, PLAYER_ONE)
        self.ai_2 = AI(self.game, PLAYER_TWO)

    def one_player_chosen(self):
        """ handles the situation when one_player button """
        self.one_player.place_forget()
        self.auto_game.place_forget()
        self.two_players.place_forget()
        self.you_start.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.cpu_start.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.you_start.bind("<Enter>", self.on_enter_player)
        self.you_start.bind("<Leave>", self.on_leave_player)
        self.cpu_start.bind("<Enter>", self.on_enter_cpu)
        self.cpu_start.bind("<Leave>", self.on_leave_cpu)
        self.return_button.place(relx=0.5, rely=0.6, anchor=CENTER)

    def on_enter_player(self,event):
        self.you_start.configure(text='PLAYER VS PC')
    def on_leave_player(self,event):
        self.you_start.configure(text='YOU START')
    def on_enter_cpu(self,event):
        self.cpu_start.configure(text='PC VS PLAYER')
    def on_leave_cpu(self,event):
        self.cpu_start.configure(text='COMPUTER START')
    def two_players_chosen(self):
        """ handles the situation when one_player button """
        self.one_player.place_forget()
        self.auto_game.place_forget()
        self.two_players.place_forget()
        self.main_canvas.pack_forget()
        self.title.pack_forget()
        player_1, player_2 = self.game.get_players()[0], \
                             self.game.get_players()[1]
        player_1.set_mode(MANUAL)
        player_2.set_mode(MANUAL)

    def prepare_board(self):
        """ pack the board into the root """
        self.turn_manager.pack(expand=YES, fill=BOTH)
        self.board_canvas.pack(expand=YES, fill=BOTH)
        self.title.pack_forget()
        self.player_1_title.place(relx=0.2, rely=0.5,anchor=CENTER)
        self.turn_message.place(relx=0.5, rely=0.5,anchor=CENTER)
        self.player_2_title.place(relx=0.8, rely=0.5,anchor=CENTER)

    def click_and_play(self, event):
        """ connects between the game and the gui objects. get a click
        from the user and runs the game accordingly. or, if the user is ai,
        runs the game with a column received from the ai. """
        current_mode = self.game.get_current_player_object().get_mode()
        if current_mode == MANUAL:
            column = self.translate_event_to_col(event)
        else:
            self.board_canvas.unbind('<Button-1>')
            cur_player = self.game.get_current_player()
            if cur_player == int(PLAYER_ONE):
                try:
                    column = self.ai_1.find_legal_move()
                except:
                    raise Illegal_move
            else:
                try:
                    column = self.ai_2.find_legal_move()
                except:
                    raise Illegal_move
        try:
            self.game.make_move(column)
            last_disc = self.game.get_discs_list()[-1]
            i, j = last_disc.get_location()
            color = last_disc.get_color()
            self.make_move_in_gui(i, j, color)

        except:
            self.popup_msg(ERROR_MSG)



        if self.game.get_winner() in POSSIBLE_WINNERS:
            self.turn_message.config(
                text=self.winning_display())
            self.board_canvas.unbind('<Button-1>')
            if self.game.get_end_game_status()==PLAYER_1:
                self.player_2_title.place_forget()
            elif self.game.get_end_game_status()==PLAYER_2:
                self.player_1_title.place_forget()

            self.mark_discs()
            self.game.set_game_over(True)
            if current_mode == AUTO:
                raise Winning_exception

    def mark_discs(self):
        """ marks the winning disc """
        if self.game.get_end_game_status()==PLAYER_1:
            color=BLUE
        else:
            color=RED
        for coordinates in self.game.get_win_list():
            i, j = coordinates

            self.board_canvas.itemconfig(self.oval_list[i][j],
                                         fill='saddle brown',
                                         outline=color,width=5)

    def popup_msg(self, msg):
        """ changes the msg displays on the screen """
        if self.game.get_end_game_status()==EMPTY_STR:
            self.turn_message.config(text=msg)
            self.turn_manager.after(700, lambda:
            self.turn_message.config(text=self.turn_display()))

    def make_move_in_gui(self, i, j, color):
        """ makes a move on the board of the gui object """
        self.board_canvas.itemconfig(self.oval_list[i][j],
                                     fill=color)

        self.turn_message.config(text=self.turn_display())

    def create_ovals(self):
        """ creates the ovals which we can see on the board """
        x, y = 0, 0
        i, j = OVAL_BIG_R, OVAL_SMALL_R
        oval_list = []
        while j <= HEIGHT_LIMIT:
            while i <= WIDTH_LIMIT:
                oval_list.append(self.board_canvas.create_oval(x, y, i, j,
                                                               fill='white'))

                x += OVAL_BIG_R
                i += OVAL_BIG_R
            x = 0
            i = OVAL_BIG_R
            y += OVAL_SMALL_R
            j += OVAL_SMALL_R
        return oval_list

    def create_board(self):
        """ creates a matrix representing the board from the ovals """
        oval_list = self.create_ovals()
        oval_list_matrix = []
        for i in range(0, BOARD_SIZE, 7):
            oval_list_matrix.append([oval_list[i] for i in range(i, i + 7)])
        return oval_list_matrix

    def turn_display(self):
        """ determines whose player turn it is and displays it on the screen"""
        cur_player = self.game.get_current_player_object().get_name()
        if cur_player == PLAYER_1:
            return PLAYER_1_TURN_MSG
        else:
            return PLAYER_2_TURN_MSG

    def winning_display(self):
        """determines which msg to display when somebody wins """
        if self.game.get_end_game_status() == PLAYER_1:
            return PLAYER_1_WIN_MSG
        elif self.game.get_end_game_status() == PLAYER_2:
            return PLAYER_2_WIN_MSG
        else:
            return TIE_MSG

    def motion(self, event):
        """ responsible for the arrow which shows the user in which column
        he's at. """
        current_mode = self.game.get_current_player_object().get_mode()
        if current_mode == MANUAL and self.game.get_end_game_status\
                    ()==EMPTY_STR:

            column = self.translate_event_to_col(event)
            if column is not None:
                if self.game.get_current_player_object().get_name() == PLAYER_2:
                    self.board_canvas.itemconfig(self.pointer,fill=RED)
                else:
                    self.board_canvas.itemconfig(self.pointer,fill=BLUE)
                self.board_canvas.coords(self.pointer,
                                         POSSIBLE_POINTER_POSITION[column], 0,
                                         POSSIBLE_POINTER_POSITION[column], 20)

    def translate_event_to_col(self,event):
        """ receive a mouse click, and translate it to a column in the game."""
        column = None
        if event.x in range(int(OVAL_BIG_R)):
            column = 0

        elif event.x in range(int(OVAL_BIG_R), 2 * int(OVAL_BIG_R)):
            column = 1

        elif event.x in range(2 * int(OVAL_BIG_R), 3 * int(OVAL_BIG_R)):
            column = 2

        elif event.x in range(3 * int(OVAL_BIG_R), 4 * int(OVAL_BIG_R)):
            column = 3

        elif event.x in range(4 * int(OVAL_BIG_R), 5 * int(OVAL_BIG_R)):
            column = 4

        elif event.x in range(5 * int(OVAL_BIG_R), 6 * int(OVAL_BIG_R)):
            column = 5

        elif event.x in range(6 * int(OVAL_BIG_R), 7 * int(OVAL_BIG_R)):
            column = 6
        return column


