#!/usr/bin/python3

from deck import Deck
from hand import Hand
import time





class GoFish(object):
	def __init__(self):
		self.player = None
		self.npc = None
		self.deck = None
		self.start_time = 0
		self.stop_time = -1
		self.current_turn = "" # will have name of the player whose turn it is
		

	def display_prompt(self):
		"""Displays the main game UI"""
		prompt = f"""
		[+] You are playing Go Fish [+]
		[+] It is {time.asctime()}  [+]
		[+] It is your turn         [+]
		-------------------------------
		> """
		return prompt

	def deal_cards(self, hand: Hand, count = 7):
		"""Deals cards to hand"""
		if self.current_turn == "":
			print(f"[+] Dealing a fresh hand to {hand.name} [+]")
			hand.add_cards(self.deck.cut_from_top(count))
		else:
			print(f"[+] Dealing {count} card(s) to {hand.name} [+]")
			hand.add_cards(self.deck.cut_from_top(count))


	def setup_game(self):
		"""Sets up player hands and deck"""
		while not self.player:
			print(f"""[+] You are starting a new game of Go Fish [+]\n[+] The time is {time.asctime()} [+]\n------------------------\n[+] Please enter your name [+]""")
			player = input(">> ")
			self.player = Hand(player, False)
			print(f"[+] Weclome, {self.player.name} [+]")

		while not self.npc:
			print(f"""[+] Would you like to name your opponent? [+]\n----------------------""")
			ans = input(">> ")

			if ans.lower() == "yes" or ans.lower() == "y":
				print("[+] Great! What would you like to call your opponent? [+]\n--------------------\n")
				npc = input(">> ")
				self.npc = Hand(npc, True)
			elif ans.lower() == "no" or ans.lower() == "n":
				print("[+] Fair enough. Your opponent will be called Blue [+]")
				self.npc = Hand("Blue", True)
			else:
				print("[+] What are you playin' at? [+]")
		
		if self.player and self.npc:
			self.deck = Deck("Ocean")

		self.deal_cards(self.player)
		self.deal_cards(self.npc)
		

		if self.player and self.npc and self.deck:
			print("[+] Deck and hands are setup -- It's time to start [+]")
			self.start_time = time.time_ns()

		

		