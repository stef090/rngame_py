import sys
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
            self.startGame(dice1, dice2)

        def check_input(self, text):
            '''Check input and return state'''    
            return True
        
        def startGame(self, dice1, dice2):
            run = 1
            while run:
                run_prompt = input("Welcome to Dice!\n"
                                   "Would you like to throw dice? Y\\N: ")
                if run_prompt.upper() == 'N':
                        return False
                dice1.number = random.randrange(0,6)
                time.sleep(2)
                print('You threw a ' + str(dice1.number))
                dice2.number = random.randrange(0,6)
                time.sleep(2)
                print('Computer threw a ' + str(dice2.number))
        
                if dice1.number > dice2.number:
                    print('You win!')
                elif dice1.number < dice2.number:
                    print('You lose! Too bad!')
                else:
                    print('It\'s a draw!')
                
            
                
                
                
