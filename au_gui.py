#gui
import tkinter, au_classes, au_world, au_event, au_region

class AUGame:
    def __init__(self):

        self._root_window = tkinter.Tk()
        self._root_window.resizable(0, 0)
        self._root_window.wm_title('Another You')
        self._root_window.configure(background = 'Black')
        
        title_label = tkinter.Label(
            master = self._root_window, text = 'Another You', background = 'Black', fg = 'White', font = ('Helvetica', 50))

        title_label.grid(row = 0, column = 0)

        start_button = tkinter.Button(
            master = self._root_window, text = 'Start Game', font = ('Helvetica', 35), bg = 'Black', fg = 'White',
            command = self._on_start_button)

        start_button.grid(row = 2, column = 0)

        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.rowconfigure(2, weight = 1)

    def _on_start_button(self):
        self._root_window.destroy()
        self._root_window = tkinter.Tk()
        self._root_window.resizable(0, 0)
        self._root_window.wm_title('Another You')
        self._root_window.configure(background = 'Black')

        character_label = tkinter.Label(
            master = self._root_window, text = 'Before beginning, please fill out the following information about yourself.', bg = 'Black', fg = 'White')

        character_label.grid(
            row = 0, column = 0, columnspan = 2, padx = 10, pady = 10)

        name_label = tkinter.Label(
            master = self._root_window, text = 'Name:', bg = 'Black', fg = 'White')

        name_label.grid(
            row = 1, column = 0, padx = 10, pady = 10, sticky = tkinter.W)

        self._name_entry = tkinter.Entry(
            master = self._root_window, width = 20)

        self._name_entry.grid(row = 1, column = 1, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)

        self._color_label = tkinter.Label(
            master = self._root_window, text = 'Favorite Color:', bg = 'Black', fg = 'White')

        self._color_label.grid(
            row = 2, column = 0, padx = 10, pady = 10, sticky = tkinter.W)

        self._color_options = tkinter.StringVar(
            master = self._root_window)

        self._color_options.set('Red')

        self._color_choices = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple']
        self._option = tkinter.OptionMenu(
            self._root_window, self._color_options, *self._color_choices)

        self._option.grid(
            row = 2, column = 1, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)

        self._gender_label = tkinter.Label(
            master = self._root_window, text = 'Gender:', bg = 'Black', fg = 'White')

        self._gender_label.grid(
            row = 3, column = 0, padx = 10, pady = 10, sticky = tkinter.W)

        self._gender_options = tkinter.StringVar(
            master = self._root_window)

        self._gender_options.set('Male')

        self._gender_choices = ['Male', 'Female']
        self._gender_option = tkinter.OptionMenu(
            self._root_window, self._gender_options, *self._gender_choices)

        self._gender_option.grid(
            row = 3, column = 1, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        
        self._continue_button = tkinter.Button(
            master = self._root_window, text = 'Continue', command = self._on_continue_button)

        self._continue_button.grid(
            row = 4, column = 1, padx = 10, pady = 10, sticky = tkinter.S + tkinter.E)

    def get_name(self) -> str:
        return self._name

    def get_color(self) -> str:
        return self._color

    def get_gender(self) -> str:
        return self._gender

    def _on_continue_button(self):
        self._name = self._name_entry.get()
        self._color = self._color_options.get()
        self._gender = self._gender_options.get()
        if self._name == '':
            self._name = 'Robin'

        self._name = self._name[::-1]
        self._name = self._name[0].upper() + self._name[1: ]
        self._name = self._name[:-1] + self._name[-1].lower()
        self._char = au_classes.Character(self._name, self._color, self._gender)

        
        self._root_window.destroy()
        self._root_window = tkinter.Tk()
        self._root_window.resizable(0, 0)
        self._root_window.wm_title('Another You')
        self._root_window.configure(background = 'Black')

        background_label = tkinter.Label(
            master = self._root_window, text = '''Welcome to the world of another you. Who is this 'other you,' you wonder?
Well, it's you! The 'you' of another dimension, anyway.
The 'you' that you could have been. Luckily for you, though,
you were born in the superior dimension. The better parallel universe.
“Superior?” you think. “Tell me more!” I happily oblige you,
because I can read your thoughts:

Yours is the superior dimension because, through this game,
you can directly affect this parallel-you's environment and actions.
Plus, said environment is full of danger and trouble.
I know I wouldn't want to live there!  But don't worry about
any of that world's trouble affecting the real,
superior version of yourself. The connection is only one-way. Definitely. 

So, go forth, and help this poor, pathetic,
parallel you survive and thrive in this strange
alternate dimension. Good luck!''', bg = 'Black', fg = 'White')

        background_label.grid(
            row = 0, column = 0)

        second_continue_button = tkinter.Button(
            master = self._root_window, text = 'Continue', bg = 'Black', fg = 'White',
            command = self._on_continue_again_button)

        second_continue_button.grid(
            row = 1, column = 0)

    def _on_continue_again_button(self): 
        self._root_window.destroy()
        self._root_window = tkinter.Tk()
        self._root_window.resizable(0, 0)
        self._root_window.wm_title('Another You')
        self._root_window.configure(background = 'Black')
        
        self._canvas = tkinter.Canvas(
            master = self._root_window, width = 530, height = 410,
            background = 'Black')

        self._photo = tkinter.PhotoImage(file = 'map.gif')

        self._canvas.create_image(265, 205, image = self._photo)

        self._canvas.grid(row = 1, column = 0)

        self._character_label = tkinter.Label(
            master = self._root_window, text = 'mp: {}     str: {}     cha: {}     events completed: {}'.format(
                self._char._mp, self._char._str, self._char._cha, self._char._events), background = 'Black', fg = 'White')

        self._character_label.grid(row = 0, column = 0, sticky = tkinter.W)

        self._root_window.columnconfigure(0, weight = 1)
        self._root_window.rowconfigure(0, weight = 1)

        self._health_label = tkinter.Label(
            master = self._root_window, text = 'hp: {}'.format(self._char._hp), background = 'Black', fg = 'White')

        self._health_label.grid(row = 0, column = 1)

        self._button_frame = tkinter.Frame(
            master = self._root_window, background = 'Black')

        self._button_frame.grid(
            row = 0, column = 1, rowspan = 2)

        self._begin_journey_button = tkinter.Button(
            master = self._button_frame, text = 'Begin Journey', bg = 'Black', fg = 'White',
            command = self._on_journey_button)

        self._begin_journey_button.grid(
            row = 0, column = 0)

    def _on_journey_button(self):
        self._root_window.destroy()
        self._root_window = tkinter.Tk()
        self._root_window.resizable(0, 0)
        self._root_window.wm_title('Another You')
        self._root_window.configure(background = 'Black')

        self._character_label = tkinter.Label(
            master = self._root_window, text = 'mp: {}     str: {}     cha: {}     events completed: {}'.format(
                self._char._mp, self._char._str, self._char._cha, self._char._events), background = 'Black', fg = 'White')

        self._character_label.grid(row = 0, column = 0, sticky = tkinter.W)

        self._root_window.columnconfigure(0, weight = 1)
        self._root_window.rowconfigure(0, weight = 1)

        self._health_label = tkinter.Label(
            master = self._root_window, text = 'hp: {}'.format(self._char._hp), background = 'Black', fg = 'White')

        self._health_label.grid(row = 0, column = 1)

        self._created_label = tkinter.Label(
            master = self._root_window, text = 'Your Journey has been created!', font = ('Ariel', 20), bg = 'Black', fg = 'White')

        self._created_label.grid(row = 1, column = 0)

        self._next_event_button = tkinter.Button(
            master = self._root_window, text = 'Next Event', bg = 'Black', fg = 'White', command = self._on_next_event)

        self._next_event_button.grid(row = 1, column = 1)

        self._world = au_world.World(self._char)

        self._world.begin_journey("test")

    def _on_next_event(self):
        self._root_window.destroy()
        self._root_window = tkinter.Tk()
        self._root_window.resizable(0, 0)
        self._root_window.wm_title('Another You')
        self._root_window.configure(background = 'Black')

        self._character_label = tkinter.Label(
            master = self._root_window, text = 'mp: {}     str: {}     cha: {}     events completed: {}'.format(
                self._char._mp, self._char._str, self._char._cha, self._char._events), background = 'Black', fg = 'White')

        self._character_label.grid(row = 0, column = 0, sticky = tkinter.W)

        self._health_label = tkinter.Label(
            master = self._root_window, text = 'hp: {}'.format(self._char._hp), background = 'Black', fg = 'White')

        self._health_label.grid(row = 0, column = 1)

        self._root_window.columnconfigure(0, weight = 1)
        self._root_window.rowconfigure(0, weight = 1)

        try:
            self._event = self._world.next_event()

            self._intro_label = tkinter.Label(
                master = self._root_window, text = self._event.get_intro_text(), font = ('Ariel', 20), bg = 'Black', fg = 'White', justify = tkinter.LEFT)

            self._intro_label.grid(row = 1, column = 0)

    #######
    ##       row 2 column 0 should be an image     
    ##        self._picture_label = tkinter.Label(
    ##            master = self._root_window, image = img)
    ##
    ##        self._picture_label.grid(row = 2, column = 0)
                
            self._options = self._event.get_options()
            self._option_one_button = tkinter.Button(
                master = self._root_window, text = self._options[0], font = ('Ariel', 16),
                bg = 'Black', fg = 'White', command = self._on_option_one)

            self._option_one_button.grid(row= 3, column = 0)

            self._option_two_button = tkinter.Button(
                master = self._root_window, text = self._options[1], font = ('Ariel', 16),
                bg = 'Black', fg = 'White', command = self._on_option_two)

            self._option_two_button.grid(row= 4, column = 0)

            self._option_three_button = tkinter.Button(
                master = self._root_window, text = self._options[2], font = ('Ariel', 16),
                bg = 'Black', fg = 'White', command = self._on_option_three)

            self._option_three_button.grid(row= 5, column = 0)
        except AttributeError:
            self._on_journey_finished()


    def _on_option_one(self):
        self._root_window.destroy()
        self._root_window = tkinter.Tk()
        self._root_window.resizable(0, 0)
        self._root_window.wm_title('Another You')
        self._root_window.configure(background = 'Black')


        self._outcome_display = tkinter.Label(
            master = self._root_window, text = self._event.select_option(0), font = ('Ariel', 20), bg = 'Black', fg = 'White')

        self._outcome_display.grid(row = 1, column = 0)

        self._character_label = tkinter.Label(
            master = self._root_window, text = 'mp: {}     str: {}     cha: {}     events completed: {}'.format(
                self._char._mp, self._char._str, self._char._cha, self._char._events), background = 'Black', fg = 'White')

        self._character_label.grid(row = 0, column = 0, sticky = tkinter.W)
        
        self._health_label = tkinter.Label(
            master = self._root_window, text = 'hp: {}'.format(self._char._hp), background = 'Black', fg = 'White')

        self._health_label.grid(row = 0, column = 1)

        self._root_window.columnconfigure(0, weight = 1)
        self._root_window.rowconfigure(0, weight = 1)

        self._next_event_button = tkinter.Button(
            master = self._root_window, text = 'Next Event', bg = 'Black', fg = 'White', command = self._on_next_event)

        self._next_event_button.grid(row = 1, column = 1)

    def _on_option_two(self):
        self._root_window.destroy()
        self._root_window = tkinter.Tk()
        self._root_window.resizable(0, 0)
        self._root_window.wm_title('Another You')
        self._root_window.configure(background = 'Black')

        self._outcome_display = tkinter.Label(
            master = self._root_window, text = self._event.select_option(1), font = ('Ariel', 20), bg = 'Black', fg = 'White')

        self._outcome_display.grid(row = 1, column = 0)

        self._character_label = tkinter.Label(
            master = self._root_window, text = 'mp: {}     str: {}     cha: {}     events completed: {}'.format(
                self._char._mp, self._char._str, self._char._cha, self._char._events), background = 'Black', fg = 'White')

        self._character_label.grid(row = 0, column = 0, sticky = tkinter.W)
        
        self._health_label = tkinter.Label(
            master = self._root_window, text = 'hp: {}'.format(self._char._hp), background = 'Black', fg = 'White')

        self._health_label.grid(row = 0, column = 1)

        self._root_window.columnconfigure(0, weight = 1)
        self._root_window.rowconfigure(0, weight = 1)

        self._next_event_button = tkinter.Button(
            master = self._root_window, text = 'Next Event', bg = 'Black', fg = 'White', command = self._on_next_event)

        self._next_event_button.grid(row = 1, column = 1)

    def _on_option_three(self):
        self._root_window.destroy()
        self._root_window = tkinter.Tk()
        self._root_window.resizable(0, 0)
        self._root_window.wm_title('Another You')
        self._root_window.configure(background = 'Black')

        self._outcome_display = tkinter.Label(
            master = self._root_window, text = self._event.select_option(2), font = ('Ariel', 20), bg = 'Black', fg = 'White')

        self._outcome_display.grid(row = 1, column = 0)

        self._character_label = tkinter.Label(
            master = self._root_window, text = 'mp: {}     str: {}     cha: {}     events completed: {}'.format(
                self._char._mp, self._char._str, self._char._cha, self._char._events), background = 'Black', fg = 'White')

        self._character_label.grid(row = 0, column = 0, sticky = tkinter.W)
        
        self._health_label = tkinter.Label(
            master = self._root_window, text = 'hp: {}'.format(self._char._hp), background = 'Black', fg = 'White')

        self._health_label.grid(row = 0, column = 1)

        self._root_window.columnconfigure(0, weight = 1)
        self._root_window.rowconfigure(0, weight = 1)

        self._next_event_button = tkinter.Button(
            master = self._root_window, text = 'Next Event', bg = 'Black', fg = 'White', command = self._on_next_event)

        self._next_event_button.grid(row = 1, column = 1)

    def _on_journey_finished(self):
        self._root_window.destroy()
        self._root_window = tkinter.Tk()
        self._root_window.resizable(0, 0)
        self._root_window.wm_title('Another You')
        self._root_window.configure(background = 'Black')

        self._finished_label = tkinter.Label(
            master = self._root_window, text = 'Your journey with {} has come to an end... for now!\nRestart the game to experience another way your journey could have unfolded!'.format(self._char._name), font = ('Ariel', 20), bg = 'Black', fg = 'White')

        self._finished_label.grid(row = 1, column = 0)
        
if __name__ == '__main__':
    AUGame()
