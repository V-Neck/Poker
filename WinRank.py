from Player import Player
from Deck import Deck
import collections

def rank(hand):
	"""
	Takes a list of card objects, converts them into tuples, 
	   sorts them, and then passes them through various functions
	   and if statements until it can assess what kind of hand it is,
	   and then assigns that list an absolute rank, used to determine the 
	   winner of a hand, and a tie breaker, which is the value of the highest
	   card in the list. Returns a tuple (rank, tie).
	"""

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

def straights(hand):
	"""Requires cards to be ordered. Takes list of card tuples (rank, suit),
	   and returns any line of consecutive cards as the length of the line
	   and the position of the last element. It also checks if the cards in
	   the line are of the same suit. Returns (length, boolean, position) """
	 #NOTE Consider revising, to accept card objects
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
	#Checks if all the cards in 'suits' are the same, and returns a boolean
	if(len(set(suits)) == 1):
		return True
	return False

def n_ofa_kind(ranks):
	#Similar to Straights, only returns lines of identically ranked cards.
	#Returns tuple (length, position)
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

