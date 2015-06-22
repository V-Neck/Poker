ranks = ['Ace','Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten','Jack','Queen','King']
suits = ["Spades","Clubs","Hearts","Diamonds"]

class Card:
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

	def get_rank(self):
		return ranks[self.rank]

	def get_suit(self):
		return suits[self.suit]