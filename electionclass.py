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
		loss_threshold = min(t.count_ballots() for t in self.list_candidates)
		for cand in self.list_candidates:
			if cand.count_ballots() == loss_threshold:
				cand.isInRunning = False

	def pass_votes (self):
		losers = [t for t in self.list_candidates if not self.list_candidates[t].isInRunning]
		for non_candidate in losers:
			for ballot in non_candidate.ballots:
				while not self.list_candidates[ballot.owner].isInRunning:
					self.list_candidates[ballot.owner].take_ballot(ballot)
					ballot.owner += 1
					self.list_candidates[ballot.owner].give_ballot(ballot)



'''		
var = genFile(reader)
instruction, value = var
if instruction == 'Candidate':
	list_candidates += [Candidate(value)]
if instruction == 'Ballot':
	list_ballots += [Ballot(value)]

instruction = var[0]
value = var[1]


variable = next(generator)
