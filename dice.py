import sys
from tkinter import *
import random
import time

class Dice(object):

    _name = 'Dice'

    def __init__(self):
        self.number = 0


class DiceGame(object):
    _name = 'Dice Game'

    def __init__(self):
        dice1 = Dice()
        dice2 = Dice()
        self.score = {'player': 0,
                      'computer': 0}
        self.startGame(dice1, dice2)

    def check_input(self, text):
        states = {'N': False,
                  'Y': True}
        return states.get(text)

    def startGame(self, dice1, dice2):
        run = 1
        print("Welcome to Dice!")
        while run:
            run_prompt = ''
            while run_prompt not in ('N','Y'):
                run_prompt = str(input("Would you like to throw dice? (Y\\N)")).upper()
            if not self.check_input(run_prompt.upper()):
                print("The score is: Player "
                      + str(self.score['player'])
                      + " : "
                      + str(self.score['computer'])
                      + " Computer")
                break
            dice1.number = random.randrange(0,6)
            time.sleep(2)
            print('You threw a ' + str(dice1.number))
            dice2.number = random.randrange(0,6)
            time.sleep(2)
            print('Computer threw a ' + str(dice2.number))

            if dice1.number > dice2.number:
                self.score['player'] += 1
                print('You win!')
            elif dice1.number < dice2.number:
                self.score['computer'] += 1
                print('You lose! Too bad!')
            else:
                print('It\'s a draw!')


class Display(object):

    def __init__(self, master):
        def yes_button_click(event):
            play_label["text"] = 'Very well!'
            print('Very well!')
        def no_button_click(event):
            play_label["text"] = 'See you later!'
            print('See you later!')

        frame_upper = Frame(master)
        frame_upper.pack()
        game_label = Label(frame_upper, text='Welcome to Dice!')
        game_label.pack()
        frame_lower = Frame(master)
        frame_lower.pack(side=BOTTOM)
        play_label = Label(frame_upper, text='Would you like to play dice?', foreground='blue')
        play_label.pack()
        player_label = Label(frame_lower, text='Player', foreground='blue', pady=20)
        computer_label = Label(frame_lower, text='Computer', foreground='red', pady=20)
        player_label.pack(side=LEFT)
        computer_label.pack(side=RIGHT)
        yes_button = Button(frame_upper, text='Yes', fg='blue', padx=5)
        no_button = Button(frame_upper, text='No', fg='red', padx=5)
        yes_button.bind("<Button-1>", yes_button_click)
        no_button.bind("<Button-1>", no_button_click)
        yes_button.pack(side=LEFT)
        no_button.pack(side=RIGHT)
        master.minsize(width=300, height=300)
        master.mainloop()



root = Tk()
Display(root)