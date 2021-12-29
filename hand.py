#!/usr/bin/python3


class Hand(object):
    def __init__(self, name: str, npc: bool):
        """Initializes a new hand with a name, 
        a bool value indicating NPC or not,
        an empty list of cards"""
        self.name = name
        self.is_npc = npc
        self.cards = [str]
        self.books = [list] # matches go here
        return
    
    def show_hand(self):
        """Prints the cards in the hand"""
        for card in self.cards:
            print(card, )
        return

    def handle_matches_in_hand(self):
        """Will check for any matches in the hand and
        then add them to the books list"""
        temp = [str]

        for x in range(0, len(self.cards) - 1):
            prime_card = self.cards[x]
            count = 0
            for y in range(x + 1, len(self.cards)):
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
    
    
    