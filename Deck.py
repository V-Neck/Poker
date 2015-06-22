from Card import Card
import random

class Deck:
	suits = ["Spades","Clubs","Hearts","Diamonds"]
	ranks = ['Ace','Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten','Jack','Queen','King']

	def __init__(self):
		self.cards = [Card(i/13, i%13) for i in range(0,52) ] 

	def shuffle(self):
		random.shuffle(self.cards)

	def draw(self):
		return self.cards.pop()

	def renew(self):
		self.cards = [Card(self.suits[i/13], self.ranks[i%13]) for i in range(0,52) ] 
