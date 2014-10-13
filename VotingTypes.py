#!python3
'''
	cameron miller ccm2493
	Esther Schenau 
	
	Voting Data Structures
'''

class Ballot (object):
	'''
	'''
	def __init__ (self, preferences):
		'''
		'''
		self.votes = tuple(preferences)
		self.owner = 0
		candidates[self.votes[self.owner]].give_ballot(self)
	
	def __iter__ (self):
		'''
		'''
		return self
	
	def __next__ (self):
		'''
		'''
		while not candidates[self.votes[self.owner]].isInRunning:
			candidates[self.votes[self.owner]].take_ballot(self)
			self.owner += 1
			candidates[self.votes[self.owner]].give_ballot(self)

