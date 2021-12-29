#!/usr/bin/python3
from gofish import GoFish
import time

def main():

    game = GoFish()

    game.setup_game()

    while game.deck.get_count != 0:
        while game.current_turn == game.player.name:
            # Do Stuff
            game.current_turn = game.npc.name
        
        while game.current_turn == game.npc.name:
            # Do Stuff
            game.current_turn = game.player.name

    game.end_game()
    

        

if __name__ == "__main__":
	main()