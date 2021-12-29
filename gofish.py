#!/usr/bin/python3

from deck import Deck
from hand import Hand
import time





class GoFish(object):
	def __init__(self):
		self.player = Hand()
		self.npc = Hand()
		self.deck = Deck()
		self.start_time = 0
		self.stop_time = -1
		self.current_turn = "" # will have name of the player whose turn it is
	

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
		while self.player.name == "":
			print(f"""[+] You are starting a new game of Go Fish [+]\n[+] The time is {time.asctime()} [+]\n------------------------\n[+] Please enter your name [+]""")
			player = input(">> ")
			self.player.name = player
			self.player.is_npc = False
			print(f"[+] Weclome, {self.player.name} [+]")

		while self.npc.name == "":
			print(f"""[+] Would you like to name your opponent? [+]\n----------------------""")
			ans = input(">> ")

			if ans.lower() == "yes" or ans.lower() == "y":
				print("[+] Great! What would you like to call your opponent? [+]\n--------------------\n")
				npc = input(">> ")
				self.npc.name = npc
				self.npc.is_npc = True
			elif ans.lower() == "no" or ans.lower() == "n":
				print("[+] Fair enough. Your opponent will be called Blue [+]")
				self.npc.name = "Blue"
				self.npc.is_npc = True
			else:
				print("[+] What are you playin' at? [+]")
		
		if self.player != "" and self.npc != "":
			self.deck = Deck("Ocean")

		print(f"[+] Shuffling the {self.deck.name} deck [+]")
		self.deck.shuffle()

		self.deal_cards(self.player)
		self.deal_cards(self.npc)
		

		if self.player and self.npc and self.deck:
			print("[+] Deck and hands are setup -- It's time to start [+]")
			self.start_time = time.time_ns()

	def end_game(self):
		"""Carries out final steps of game,
		including score"""

		self.stop_time = time.time_ns()
		total_time = (self.stop_time - self.start_time) / 60000000000

		if len(self.player.books) > len(self.npc.books):
			winner = self.player.name + f" with {len(self.player.books)} books!"
		elif len(self.player.books) < len(self.npc.books):
			winner = self.npc.name + f" with {len(self.npc.books)} books!"
		else:
			winner = "... actually, it was a tie lol"

		print(f"""
			[+] The game is over! [+]
			[+] The winner is {winner} [+]
			[+] It took {total_time} minutes -- wow [+]""")

	def handle_player_fishing(self, fish):
		"""Handles a fishing request from the player.
		This must be in the form of 'Do you have any Xs?',
		otherwise, will throw an error."""
		request = "Do you have any "
		if request not in fish:
			print("[-] You need to ask the right way or else we just won't get anywhere [-]")
			return 0
		else:
			requested_card = fish.split(request)[1].split("s?")

			if requested_card[0].lower() == "two" or requested_card[0] == "2":
				count = 0
				for card in self.npc.cards:
					if "2" in card:
						self.player.add_card(card)
						self.npc.discard_card(card)
						count += 1
				if count > 0:
					print(f"{self.npc.name}: Yep :| ")
					print(f"[+] {self.player.name} received {count} cards from {self.npc.name} [+]")
					return 1
				else:
					print(f"{self.npc.name}: Nope! Go fish!")
					self.player.add_card(self.deck.cut_from_top(1))
					print(f"[-] {self.player.name} had to draw a card from the {self.deck.name} deck [-]")
					return 1
			elif requested_card[0].lower() == "three" or requested_card[0] == "3":
				count = 0
				for card in self.npc.cards:
					if "3" in card:
						self.player.add_card(card)
						self.npc.discard_card(card)
						count += 1
				if count > 0:
					print(f"{self.npc.name}: Yep :| ")
					print(f"[+] {self.player.name} received {count} cards from {self.npc.name} [+]")
					return 1
				else:
					print(f"{self.npc.name}: Nope! Go fish!")
					self.player.add_card(self.deck.cut_from_top(1))
					print(f"[-] {self.player.name} had to draw a card from the {self.deck.name} deck [-]")
					return 1
			elif requested_card[0].lower() == "four" or requested_card[0] == "4":
				count = 0
				for card in self.npc.cards:
					if "4" in card:
						self.player.add_card(card)
						self.npc.discard_card(card)
						count += 1
				if count > 0:
					print(f"{self.npc.name}: Yep :| ")
					print(f"[+] {self.player.name} received {count} cards from {self.npc.name} [+]")
					return 1
				else:
					print(f"{self.npc.name}: Nope! Go fish!")
					self.player.add_card(self.deck.cut_from_top(1))
					print(f"[-] {self.player.name} had to draw a card from the {self.deck.name} deck [-]")
					return 1
			elif requested_card[0].lower() == "five" or requested_card[0] == "5":
				count = 0
				for card in self.npc.cards:
					if "5" in card:
						self.player.add_card(card)
						self.npc.discard_card(card)
						count += 1
				if count > 0:
					print(f"{self.npc.name}: Yep :| ")
					print(f"[+] {self.player.name} received {count} cards from {self.npc.name} [+]")
					return 1
				else:
					print(f"{self.npc.name}: Nope! Go fish!")
					self.player.add_card(self.deck.cut_from_top(1))
					print(f"[-] {self.player.name} had to draw a card from the {self.deck.name} deck [-]")
					return 1
			elif "six" in requested_card[0].lower() or requested_card[0] == "6":
				count = 0
				for card in self.npc.cards:
					if "6" in card:
						self.player.add_card(card)
						self.npc.discard_card(card)
						count += 1
				if count > 0:
					print(f"{self.npc.name}: Yep :| ")
					print(f"[+] {self.player.name} received {count} cards from {self.npc.name} [+]")
					return 1
				else:
					print(f"{self.npc.name}: Nope! Go fish!")
					self.player.add_card(self.deck.cut_from_top(1))
					print(f"[-] {self.player.name} had to draw a card from the {self.deck.name} deck [-]")
					return 1
			elif requested_card[0].lower() == "seven" or requested_card[0] == "7":
				count = 0
				for card in self.npc.cards:
					if "7" in card:
						self.player.add_card(card)
						self.npc.discard_card(card)
						count += 1
				if count > 0:
					print(f"{self.npc.name}: Yep :| ")
					print(f"[+] {self.player.name} received {count} cards from {self.npc.name} [+]")
					return 1
				else:
					print(f"{self.npc.name}: Nope! Go fish!")
					self.player.add_card(self.deck.cut_from_top(1))
					print(f"[-] {self.player.name} had to draw a card from the {self.deck.name} deck [-]")
					return 1
			elif requested_card[0].lower() == "eight" or requested_card[0] == "8":
				count = 0
				for card in self.npc.cards:
					if "8" in card:
						self.player.add_card(card)
						self.npc.discard_card(card)
						count += 1
				if count > 0:
					print(f"{self.npc.name}: Yep :| ")
					print(f"[+] {self.player.name} received {count} cards from {self.npc.name} [+]")
					return 1
				else:
					print(f"{self.npc.name}: Nope! Go fish!")
					self.player.add_card(self.deck.cut_from_top(1))
					print(f"[-] {self.player.name} had to draw a card from the {self.deck.name} deck [-]")
					return 1
			elif requested_card[0].lower() == "nine" or requested_card[0] == "9":
				count = 0
				for card in self.npc.cards:
					if "9" in card:
						self.player.add_card(card)
						self.npc.discard_card(card)
						count += 1
				if count > 0:
					print(f"{self.npc.name}: Yep :| ")
					print(f"[+] {self.player.name} received {count} cards from {self.npc.name} [+]")
					return 1
				else:
					print(f"{self.npc.name}: Nope! Go fish!")
					self.player.add_card(self.deck.cut_from_top(1))
					print(f"[-] {self.player.name} had to draw a card from the {self.deck.name} deck [-]")
					return 1
			elif requested_card[0].lower() == "ten" or requested_card[0] == "10":
				count = 0
				for card in self.npc.cards:
					if "10" in card:
						self.player.add_card(card)
						self.npc.discard_card(card)
						count += 1
				if count > 0:
					print(f"{self.npc.name}: Yep :| ")
					print(f"[+] {self.player.name} received {count} cards from {self.npc.name} [+]")
					return 1
				else:
					print(f"{self.npc.name}: Nope! Go fish!")
					self.player.add_card(self.deck.cut_from_top(1))
					print(f"[-] {self.player.name} had to draw a card from the {self.deck.name} deck [-]")
					return 1
			elif requested_card[0].lower() == "jack" or requested_card[0].upper() == "J":
				count = 0
				for card in self.npc.cards:
					if "J" in card:
						self.player.add_card(card)
						self.npc.discard_card(card)
						count += 1
				if count > 0:
					print(f"{self.npc.name}: Yep :| ")
					print(f"[+] {self.player.name} received {count} cards from {self.npc.name} [+]")
					return 1
				else:
					print(f"{self.npc.name}: Nope! Go fish!")
					self.player.add_card(self.deck.cut_from_top(1))
					print(f"[-] {self.player.name} had to draw a card from the {self.deck.name} deck [-]")
					return 1
			elif requested_card[0].lower() == "queen" or requested_card[0].upper() == "Q":
				count = 0
				for card in self.npc.cards:
					if "Q" in card:
						self.player.add_card(card)
						self.npc.discard_card(card)
						count += 1
				if count > 0:
					print(f"{self.npc.name}: Yep :| ")
					print(f"[+] {self.player.name} received {count} cards from {self.npc.name} [+]")
					return 1
				else:
					print(f"{self.npc.name}: Nope! Go fish!")
					self.player.add_card(self.deck.cut_from_top(1))
					print(f"[-] {self.player.name} had to draw a card from the {self.deck.name} deck [-]")
					return 1
			elif requested_card[0].lower() == "king" or requested_card[0].upper() == "K":
				count = 0
				for card in self.npc.cards:
					if "K" in card:
						self.player.add_card(card)
						self.npc.discard_card(card)
						count += 1
				if count > 0:
					print(f"{self.npc.name}: Yep :| ")
					print(f"[+] {self.player.name} received {count} cards from {self.npc.name} [+]")
					return 1
				else:
					print(f"{self.npc.name}: Nope! Go fish!")
					self.player.add_card(self.deck.cut_from_top(1))
					print(f"[-] {self.player.name} had to draw a card from the {self.deck.name} deck [-]")
					return 1
			elif requested_card[0].lower() == "ace" or requested_card[0].upper() == "A":
				count = 0
				for card in self.npc.cards:
					if "A" in card:
						self.player.add_card(card)
						self.npc.discard_card(card)
						count += 1
				if count > 0:
					print(f"{self.npc.name}: Yep :| ")
					print(f"[+] {self.player.name} received {count} cards from {self.npc.name} [+]")
					return 1
				else:
					print(f"{self.npc.name}: Nope! Go fish!")
					self.player.add_card(self.deck.cut_from_top(1))
					print(f"[-] {self.player.name} had to draw a card from the {self.deck.name} deck [-]")
					return 1
			else:
				print("[-] What are you even trying to do right now? [-]")
				return 0


		