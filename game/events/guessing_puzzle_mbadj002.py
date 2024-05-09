from game import event
from game.player import Player
import game.config as config
import random
guess_range = 10
num = random.randint(1,guess_range)
print (num)

class Sphinx (event.Event):
    """Enconter a gaurdian sphinx in the midst of the jungle. You must play its guessing game to pass.
    The Sphinx will think of a number between 1-10 and you must guess the correct number to move on. The sphinx will tell you whether or not your guesses are too big, 
    too small or correct. """

    def __init__ (self):
        self.name = "gaurdian Sphinx"
       

    def process (self, world):
    # Welcome pirates to the puzzle
        print(f"You have encountered the jungle Sphinx. You must solve his puzzle")
        guess = int(input("The sphinx wants you to guess a number between 1-10. Or DIE!: "))


    # Set up conditions for how the sphinx will react based on certain guesses made
    # Have this be a loop to have user keep guessing until the right guess is made
        while num != guess:
            if guess < num:
                print(f"The Sphinx says that is too small. Guess again!")
                guess = int(input("Guess a number from 1-10: "))
            elif guess > num:
                print(f"The Sphinx says that is too big. Guess again!")
                guess = int(input("Guess a number from 1-10: "))
        print("The Sphinx Congratulates you! Thats the correct guess. You are allowed to pass.")