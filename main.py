#!/usr/bin/python3
from gofish import GoFish
import time

def main():

    game_prompt = f"""
		[+] You are playing Go Fish [+]
		[+] It is {time.asctime()}  [+]
		[+] It is your turn         [+]
		-------------------------------
		> """

    game = GoFish()

    game.setup_game()

    if game.start_time % 2 == 0:
        game.current_turn = game.player.name
    else:
        game.current_turn = game.npc.name

    while game.deck.get_count != 0:
        while game.current_turn == game.player.name:
            game.player.show_hand()
            game.player.handle_matches_in_hand()
            while True:
                fish = input(game_prompt)
                if game.handle_player_fishing(fish) != -1:
                    game.player.handle_matches_in_hand()
                    break

            game.current_turn = game.npc.name
        
        while game.current_turn == game.npc.name:
            # Do Stuff
            game.current_turn = game.player.name

    game.end_game()
    

        

if __name__ == "__main__":
	main()