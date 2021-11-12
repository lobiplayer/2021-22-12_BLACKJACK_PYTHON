import random

def create_deck():
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
            'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
            'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

    # CARD
    # SUIT, RANK, VALUE


    class Card():

        def __init__(self, suit, rank):
            self.suit = suit
            self.rank = rank
            self.value = values[rank]

        def __str__(self):
            return self.rank + ' of ' + self.suit


    def make_deck(suits, ranks):
        deck = []
        for suit in suits:
            for rank in ranks:
                deck.append(Card(suit, rank))
        return deck
    
    return make_deck(suits, ranks)

def create_shuffeled_deck():
    new_deck = create_deck()

    random.shuffle(new_deck)

    return new_deck