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

#DiceGame()
root = Tk()
frameUpper = Frame(root)
frameUpper.pack()
gameLabel = Label(frameUpper, text='Welcome to Dice!')
gameLabel.pack()
frameLower = Frame(root)
frameLower.pack(side=BOTTOM)
playLabel = Label(frameUpper, text='Would you like to play dice?', foreground='blue')
playLabel.pack()
yesButton = Button(frameUpper, text='Yes', fg='blue', padx=5)
noButton = Button(frameUpper, text='No', fg='red', padx = 5)
yesButton.pack(side=LEFT)
noButton.pack(side=RIGHT)
root.minsize(width=300, height=300)
root.mainloop()