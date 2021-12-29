#!/usr/bin/python3

import time

class Deck(object):
	"""A deck of cards"""
	def __init__(self, name: str):
		"""Initialize the object
		Should create a list of cards (ex. "A♤")
		Should have a name (incase multiple decks are initialized)"""
		self.name = name
		suits = ["♤", "♡", "♧", "♢"]
		self.deck = []
		for suit in suits:
			self.deck.append(f"A{suit}")
			for i in range(2,11):
				card = f"{i}{suit}"
				self.deck.append(card)
			self.deck.append(f"J{suit}")
			self.deck.append(f"Q{suit}")
			self.deck.append(f"K{suit}")
		print(f"The {self.name} deck has been created with {len(self.deck)} cards.")
		

	def shuffle(self, count=5):
		"""Takes a deck of cards and rearranges them (shuffles them)"""
		count = count
		while count != 0:
			# cut the deck
			mid = int(len(self.deck) / 2)
			first_half = self.deck[:mid]
			second_half = self.deck[mid:]
			self.deck.clear()			
	
			for i in range(0, len(first_half)):
				# handle some randomization first
				index = time.time_ns() % len(first_half)
				temp = first_half.pop()
				first_half.insert(index, temp)
				index = time.time_ns() % len(second_half)
				temp = second_half.pop()
				second_half.insert(index, temp)
				
				# then merge the halves
				self.deck.insert(0,first_half.pop())
				self.deck.insert(0,second_half.pop())
			
			count -= 1


	def cut_from_top(self, num):
		"""Takes a number and removes that amount of cards from the top of the deck"""
		if not isinstance(num, int):
			print(f"You have to provide an actual number.  What does it mean to remove \"{num}\" cards from the deck?")
		elif num > len(self.deck):
			print("You're trying to remove more cards from the deck than are in it...")
		elif num < 1:
			print("How do you expect to *remove* less than one card?")
		else:
			print(f"Okay, going to remove {num} cards from the top of the {self.name} deck.") 
			for x in range(0,num):
				self.deck.pop(x)
			
			print(f"There are now {len(self.deck)} cards in the {self.name} deck.")

	def cut_from_mid(self, num):
		"""Takes a number and removes that amount of cards from the middle of the deck"""
		return

	def cut_from_bottom(self, num):
		"""Takes a number and removes that amount of cards from the bottom of the deck"""
		return

	def get_random_card(self):
		"""Prints a card at random from the deck. Card is returned to deck"""
		return

	def get_card(self, card):
		"""Takes a card and searches the deck for it beginning at the top"""
		return

	def get_card_by_index(self, num):
		"""Takes a number that is 52 or less and returns the card at that location in the deck"""
		return

	def display(self):
		"""displays all cards in deck"""
		for i in range(0, int(len(self.deck) / 4)):
			print(self.deck[i].rjust(3, ' '), self.deck[i+13].rjust(3, ' '), self.deck[i+26].rjust(3, ' '), self.deck[i+26].rjust(3, ' '), self.deck[i+39].rjust(3, ' '))

	def get_count(self):
		return len(self.deck)