from tkinter import *
import random
import time


class DiceGame(object):
    _name = 'Dice Game'

    def __init__(self):
        self.score = {'player': 0,
                      'computer': 0}

    def throw_dice(self):
        print("Dice thrown!")
        dice_player = random.randrange(0, 6)
        dice_computer = random.randrange(0, 6)
        if dice_player > dice_computer:
            self.score["player"] += 1
        elif dice_computer > dice_player:
            self.score["computer"] += 1
        return dice_player, dice_computer, self.score


class Display(object):

    def __init__(self, master):
        game = DiceGame()

        def yes_button_click(event):
            redraw_labels()
            play_label["text"] = 'Very well!'
            notice_label["text"] = 'Dice thrown'
            result = game.throw_dice()
            player_dice_label["text"] += str(result[0])
            computer_dice_label["text"] += str(result[1])
            player_label["text"] += str(result[2]["player"])
            computer_label["text"] += str(result[2]["computer"])

        def no_button_click(event):
            play_label["text"] = 'See you later!'
            time.sleep(3)
            print('See you later!')
            root.quit()

        def redraw_labels():
            player_dice_label["text"] = 'Player Dice: '
            computer_dice_label["text"] = 'Computer Dice: '
            player_label["text"] = 'Player: '
            computer_label["text"] = 'Computer: '

        #Frame definition
        frame_upper = Frame(master)
        frame_upper.pack()
        frame_lower = Frame(master)
        frame_lower.pack(side=BOTTOM)

        #Upper Frame
        game_label = Label(frame_upper, text='Welcome to Dice!')
        game_label.grid(row=0, column=1, sticky=N)
        play_label = Label(frame_upper, text='Would you like to play dice?', foreground='blue')
        play_label.grid(row=1, column=1)
        yes_button = Button(frame_upper, text='Yes', fg='blue', padx=5)
        no_button = Button(frame_upper, text='No', fg='red', padx=5)
        yes_button.bind("<Button-1>", yes_button_click)
        no_button.bind("<Button-1>", no_button_click)
        yes_button.grid(row=2, column=0, sticky=W)
        no_button.grid(row=2, column=2, sticky=E)
        notice_label = Label(frame_upper, text='', foreground='blue')
        notice_label.grid(row=3, column=1)
        player_dice_label = Label(frame_upper, text='Player Dice: ', foreground='blue')
        computer_dice_label = Label(frame_upper, text='Computer Dice: ', foreground='red')
        player_dice_label.grid(row=4, column=0)
        computer_dice_label.grid(row=4, column=2)

        #Lower Frame
        result_label = Label(frame_lower, text='Result', pady=15)
        player_label = Label(frame_lower, text='Player: ', foreground='blue', pady=20)
        computer_label = Label(frame_lower, text='Computer: ', foreground='red', pady=20)
        result_label.grid(row=0, column=1)
        player_label.grid(row=1, column=0, sticky=W)
        computer_label.grid(row=1, column=2, sticky=E)
        master.minsize(width=300, height=300)
        master.mainloop()


root = Tk()
Display(root)
