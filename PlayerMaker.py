from sys import exit
import time

def make_player():
    
    class Player():

        def __init__(self, name, age, chips):
            self.name = name
            self.age = age
            self.chips = chips

        def __str__(self):
            return 'name: ' + self.name + ' chips: ' + str(self.chips)


    name = input('What is your name?')

    age = int(input('What is your age? (You must be 18+ to gamble) '))
    if age < 18:
        print('You are not allowed to play. This program will close now')
        time.sleep(3)
        exit()
    else:
    
        # name = 'Robin'
        # age = 25
        chips = 1000
        print('You have received a welcome bonus of $1000')

    return Player(name, age, chips)