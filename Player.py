from Deck import Deck
class Player:
	def __init__(self, name, money, deck):
		self.name = name
		self.deck = deck
		self.money = money
		self.hand = []
		self.fillHand()
		self.rank = 0

	def fillHand(self):
		self.hand = [self.deck.draw() for i in range(0,5)]

	def bet(self, amount):
		self.money -= amount
		return amount

	def win(self, amount):
		self.money += amount
		print "%s wins $%d" % (self.name, amount)

	def all_in(self):
		self.money = 0

	def print_hand(self):
		for card in self.hand:
			print "%s of %s" %( card.get_rank(), card.get_suit() )