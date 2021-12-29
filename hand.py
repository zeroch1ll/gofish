#!/usr/bin/python3


class Hand(object):
    def __init__(self, name: str, npc: bool):
        """Initializes a new hand with a name, 
        a bool value indicating NPC or not,
        an empty list of cards"""
        self.name = name
        self.is_npc = npc
        self.cards = [str]
        return
    
    def show_hand(self):
        """Prints the cards in the hand"""
        return

    def check_for_matches(self):
        """Will check for any matches in the hand"""
        return

    def discard(self, i: int):
        """Removes the card at the given index i"""
        return

    def add_card(self, card):
        """Appends a new card to the hand"""
        return

    def add_cards(self, cards):
        """Appends multiple cards to the hand"""
        return

    
    
    