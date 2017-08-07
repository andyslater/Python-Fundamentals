class Card(object):

    def __init__(self, card_value, suit=None, game_value=None):
        face_cards = {'J': 11, 'Q': 12, 'K': 13, 'A': 1}
        if game_value:
            self.game_value = game_value
        elif card_value in face_cards:
            self.game_value = face_cards[card_value]
        else:
            self.game_value = card_value
        self.card_value = str(card_value)
        self.suit = suit

    def __repr__(self):
        if self.suit:
            return ' '.join(['[', self.card_value, 'of', self.suit, ']'])
        return ' '.join(['[', self.card_value, ']'])

    def __lt__(self, other):
        """Called by comparison operators."""
        return (self.game_value < other.game_value)

    def __gt__(self, other):
        """Called by comparison operators."""
        return (self.game_value > other.game_value)



ten = Card(10, 'diamonds')
jack = Card('J', 'clubs')
queen = Card('Q', 'spades')
king = Card('K', 'hearts')
joker = Card('Joker', game_value=100)
print(ten, jack, queen, king, joker)

print('K > J:', king > jack)
print('10 < J:', ten < jack)
print('NOT J < 10:', not jack < ten)
print('Joker > K:', joker > king)
print('J < Q < K:', jack < queen < king)
