for i in players:
	i.rank = rank(i.hand)
	print "%s:" % i.name
	i.print_hand()
	print

winner(players, sum([i.bet(20) for i in players]))

deck = Deck()
deck.shuffle()
players = [Player("Bob", 20, deck), Player("Alice", 20, deck)]



def winner(players, bets):
	best = max([i.rank[0] for i in players])
	ties = [i for i in players if best == i.rank[0]]
	high = max([i.rank[1] for i in ties])
	win = [i for i in ties if high == i.rank[1]]
	for i in win:
		i.win( float(bets)/len(win) )
