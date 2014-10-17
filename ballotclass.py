class Ballot (Candidate):
	'''
	'''
	def __init__ (self, preferences):
		'''
		'''
		self.votes = tuple(preferences)
		self.owner = 0
		list_candidates[self.votes[self.owner] - 1].give_ballot(self)

	def show_ballot (self): 
		print (self.votes)

	def next_vote (self):
		while not list_candidates[self.votes[self.owner] - 1].isInRunning:
			list_candidates[self.votes[self.owner] - 1].take_ballot(self)
			self.owner += 1
			list_candidates[self.votes[self.owner] - 1].give_ballot(self)