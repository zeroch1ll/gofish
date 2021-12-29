#!/usr/bin/python3
from Deck import Deck

def main():

	deck = Deck("test")

	deck.display()
	deck.shuffle()
	print("\n")
	deck.display()

if __name__ == "__main__":
	main()