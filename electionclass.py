class Election(object): 

	def __init__(self): 
		self.list_ballots = []
		self.list_candidates = []
		self.hasWinner = False
		self.hasTie = False

	def add_candidate(self, candidate):
		self.list_candidates.append(candidate)
	
	def add_ballot(self, ballot):
		self.list_ballots.append(ballot)

	def look_for_winner (self):
		for candy in self.list_candidates:
			if candy.count_ballots() > .5 * len(self.ballots):
				self.hasWinner = True
				candy.isWinner = True
		return self.hasWinner
	
	def look_for_tie (self):
		tickity_tie = [self.list_candidates[0].count_ballots() == candy.count_ballots() for candy in self.list_candidates[1:] if candy.isInRunning]
		theresatie = True
		for thisone in tickity_tie:
			theresatie = theresatie and thisone
		if theresatie:
			for candy in self.list_candidates:
				if candy.isInRunning:
					candy.isWinner = True
		return theresatie
	
	def mark_the_losers (self):
		