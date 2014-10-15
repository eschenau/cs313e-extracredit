#!python3
'''
	cameron miller ccm2493
	Esther Schenau ees847
	
	Voting Data Structures
'''

class Ballot (object):
	'''
	'''
	def __init__ (self, *preferences):
		'''
		'''
		self.votes = tuple(preferences)
		self.owner = 0
		candidates[self.votes[self.owner] - 1].give_ballot(self)
	
	def __iter__ (self):
		'''
		'''
		return self
	
	def __next__ (self):
		'''
		'''
		while not candidates[self.votes[self.owner]].isInRunning:
			candidates[self.votes[self.owner] - 1].take_ballot(self)
			self.owner += 1
			candidates[self.votes[self.owner] - 1].give_ballot(self)

class Candidate (object):
	'''
	'''
	def __init__ (self, name):
		self.name = name
		self.ballots = set()
		self.isInRunning = True

	def give_ballot (self, ballot):
		self.ballots.add(ballot)

	def take_ballot (self, ballot):
		self.ballots.remove(ballot)

	def count_ballots (self):
		return len(self.ballots)

class Election (object):
	def __init__ (self, candidates):
		self.candidates = [Candidate(candidates[t]) for t in number_of_candidates]

def Voting_Read (reader):
	'''
	'''
	for line in reader: 
		yield line

#ESTHER to CAMERON: Don't need main function in the logic harness, put code into a separate function we import into the run harness(?)
def main ():
	"""
	number_of_elections = int(reader.readline().strip()) #pull the number of elections
	election_number = 0
	Elections = []
	


	while election_number <= number_of_elections:
		line = reader.readline().strip()
		if line == '':
			election_number += 1
			if election_number > 1:
				Elections.append(Election(t) for t in Candidates)
			continue
		try:
			number_of_candidates = int(line)
		except ValueError:
			#temporary instruction, needed to test this code
			pass

	"""
	#----- Temporary Code to Visualize-----
	print (number_of_candidates)
	print (Elections)

	main() 

