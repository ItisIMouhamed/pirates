
from game import event
import random
import game.config as config

from game.display import announce
from game.display import menu

class Large_wave (event.Event):

    def __init__ (self):
        self.name = " A large wave has appeared"


    def process (self, world):
        #Step 1: Say "A large wave has appeared!"
        #Step 2: Offer player choice between going below decks or trying to ride it out on deck
        #Step 3: If they don't go below, choose a random number from 1 to 6, on a 5 kill the pirates
        announce (self.name)

        # choice = input("Do you want to go below deck? (B) or try to ride it out on deck? (R)").upper()
        choice = menu(["Go below deck.", "Try to ride it out on deck."])

        if choice == 0:
            print("You went below deck.")
        elif choice == 1:
            num_sides = 6
            decision = random.randint(1, num_sides)
            announce (f"The dice landed on: {decision}")

            if decision == 5:
                print(f"The large wave has crashed the ship")
            else:
                print(f"The ship survived being hit by the large wave.")
        else:
            print("Invalid choice. Please choose either ")

        result = {}
        result["message"] = ""
        result["newevents"] = [ self ]
        return result


        
       