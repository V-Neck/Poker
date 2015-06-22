from Player import Player
from Deck import Deck
import collections

suits = ["Spades","Clubs","Hearts","Diamonds"]
ranks = ['Ace','Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten','Jack','Queen','King']

deck = Deck()
deck.shuffle()
players = [Player("Bob", 20, deck), Player("Alice", 20, deck)]

def rank(hand):
	#Takes a hand, orders it, and determines
	#Whether it is a flush, straight, n of a kind, etc.

	hand = sorted([(i.rank, i.get_suit()) for i in hand])
	flush = contiguous_suits([i[1] for i in hand])
	straight = straights(hand)
	of_a_kind = n_ofa_kind([i[0] for i in hand])

	if(flush):
		if 5 in [i[0] for i in straight]:
			if hand[0][0] == 8:
				return (9, hand[4][0])#"Royal Flush"

			else:
				return (8, hand[4][0]) #"Straight Flush"

		else:
			return (7, hand[4][0])#"Flush"

	else:
		if 5 in [i[0] for i in straight]:
			return (6, hand[4][0])#"Straight"

		elif 4 in [i[0] for i in of_a_kind]:
			return (5, hand[4][0])#"Four of a Kind"

		elif 3 in [i[0] for i in of_a_kind] and 2 in [i[0] for i in of_a_kind]:
			return (4, hand[4][0])#"Full House"

		elif 3 in [i[0] for i in of_a_kind]:
			return (3, hand[4][0])#"Three of a Kind"

		elif [i[0] for i in of_a_kind].count(2) == 2:
			return (2, hand[4][0])#"Two Pair"

		elif 2 in [i[0] for i in of_a_kind]:
			return (1, hand[4][0])#"One Pair"
		else: 
			return (0, hand[4][0])#"High Card"

def winner(players, bets):
	best = max([i.rank[0] for i in players])
	ties = [i for i in players if best == i.rank[0]]
	high = max([i.rank[1] for i in ties])
	win = [i for i in ties if high == i.rank[1]]
	for i in win:
		i.win( float(bets)/len(win) )


def straights(hand):
	#Takes an ordered hand, return tuple with length of straits, 
	#whether contiguous suit, and greatest card
	straight_len = 0
	straights = []
	straight_suits = []
	for i in range(0, len(hand)-1):
		if abs(hand[i][0] - hand[i+1][0]) == 1:
			straight_len +=1
			straight_suits.append(hand[i][1])
		elif straight_len > 0:
			straights.append( (straight_len+1, contiguous_suits(straight_suits),i) )
			straight_len = 0
			straight_suits = []
	straights.append( (straight_len+1, contiguous_suits(straight_suits), 4) )
	return [i for i in straights if i[0]>1]

def contiguous_suits(suits):
	if(len(set(suits)) == 1):
		return True
	return False

def n_ofa_kind(ranks):
	n_len = 0
	n_ofa_kinds = []
	for i in range(0, len(ranks)-1):
		if ranks[i] == ranks[i+1]:
			n_len +=1
		else:
			n_ofa_kinds.append( (n_len+1, i) )
			n_len = 0
	n_ofa_kinds.append( (n_len+1, 4) )
	return [i for i in n_ofa_kinds if i[0] > 1]

for i in players:
	i.rank = rank(i.hand)
	print "%s:" % i.name
	i.print_hand()
	print

winner(players, sum([i.bet(20) for i in players]))
