#!/usr/bin/python3


class Hand(object):
    def __init__(self,):
        """Initializes a new hand with a name, 
        a bool value indicating NPC or not,
        an empty list of cards"""
        self.name = ""
        self.is_npc = bool
        self.cards = []
        self.books = [] # matches go here
        
    
    def show_hand(self):
        """Prints the cards in the hand"""
        print("[>] Your current hand is: ")
        for card in self.cards:
            print(card + " ", end="")
        

    def handle_matches_in_hand(self):
        """Will check for any matches in the hand and
        then add them to the books list"""
        temp = []

        for x in range(0, len(self.cards) - 2):
            prime_card = self.cards[x]
            count = 0
            for y in range(x + 1, len(self.cards)- 1):
                second_card = self.cards[y]
                if prime_card[0] == second_card[0]:
                    temp.append(self.cards.pop(y))
                    count +=1
        
            if count > 0:
                self.add_matches(temp)
                print(f"[+] Added {count} matches to {self.name}'s books [+]")

    def discard_at_index(self, i: int):
        """Removes the card at the given index i"""
        self.cards.pop(i)
        return

    def discard_card(self, card):
        """Removes card based on value of card"""
        self.cards.remove(card)
        return

    def add_card(self, card):
        """Appends a new card to the hand"""
        self.cards.append(card)
        return

    def add_cards(self, cards):
        """Appends multiple cards to the hand"""
        for card in cards:
            self.cards.append(card)
        return

    def add_matches(self, cards):
        """Appends matches to books list"""
        if len(self.books) == 0:
            self.books.append(cards)
        else:
            card_type = cards[0][0]
            for book in self.books:
                for card in book:
                    if card_type in card:
                        book.append(cards)