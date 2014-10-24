#!/usr/bin/env/python3
#Esther Schenau, Cameron Miller

# --------------
# Election class
# --------------
class Election(object): 
	'''
	object to keep track of each unique election
	'''
	def __init__(self):
		'''
		construct an empty election object
		'''
		self.list_candidates = []
		self.list_ballots = []
		self.hasWinner = False
		self.hasTie = False
		self.winner = []
	
	def __repr__ (self):
		'''
		represent method allows visualization of data processing
		included for debugging purposes
		'''

		retstr = 'Candidates:\n'
		for candies in self.list_candidates:
			retstr += candies.name + '  Ballots: ' + str(candies.count_ballots()) + ', and is ' + (not candies.isInRunning)*'not ' + 'in the running.\n'
		retstr += '\nThere is ' + (not self.hasWinner and not self.hasTie)*'not ' + 'a winner.\n' + str(self.winner)
		return retstr

	def add_candidate(self, candidate):
		'''
		add a candidate to the election's list of candidates
		'''
		self.list_candidates.append(candidate)

	def add_ballot(self, ballot):
		'''
		add a ballot to the election's list of ballots
		'''
		self.list_ballots.append(ballot)
		self.list_candidates[ballot.votes[0] - 1].give_ballot(ballot)

	def look_for_winner (self):
		'''
		looking through election's list of candidates in running
		boolean return -- True : winner present, False : winner not present
		'''
		if len(self.list_candidates) == 1:
			self.hasWinner = True
			self.list_candidates[0].isWinner = True
			self.winner = [self.list_candidates[0].name]
		else:
			for t in range(len(self.list_candidates)):
				if not self.list_candidates[t].isInRunning:
					continue
				assert self.list_candidates
				if self.list_candidates[t].count_ballots() > .5 * len(self.list_ballots):
					self.hasWinner = True
					self.list_candidates[t].isWinner = True 
					for candidate in self.list_candidates[:t]:
						candidate.isInRunning = False
					for candidate in self.list_candidates[t + 1:]:
						candidate.isInRunning = False
					self.winner = [self.list_candidates[t].name]
		return self.hasWinner

	def look_for_tie (self):
		'''
		looks through the elections list of in running candidates and determines if there is a tie
		returns true if there is a tie
		'''
		inRunning = [t for t in self.list_candidates if t.isInRunning]
		tie_check = [inRunning[0].count_ballots() == candidate.count_ballots() for candidate in inRunning[1:]]
		theres_a_tie = True
		for check in tie_check:
			theres_a_tie = theres_a_tie and check
		if theres_a_tie:
			for candidate in self.list_candidates:
				if candidate.isInRunning:
					candidate.isWinner = True
				self.winner = [cand.name for cand in self.list_candidates if cand.isInRunning]
		self.hasTie = theres_a_tie
		return theres_a_tie

	def mark_the_losers (self):
		'''
		determines which candidates are no longer in the running
		'''
		loss_threshold = min(t.count_ballots() for t in self.list_candidates if t.isInRunning)
		for cand in self.list_candidates:
			if cand.count_ballots() <= loss_threshold:
				cand.isInRunning = False

	def pass_votes (self):
		'''
		takes ballots away from losers and gives them to the ballot's next choice of in running candidate
		'''
		losers = [t for t in self.list_candidates if not t.isInRunning]
		for non_candidate in losers:
			while not not non_candidate.ballots:
				ballot = non_candidate.ballots.pop()
				while ballot.owner < len(ballot.votes) and not self.list_candidates[ballot.votes[ballot.owner] - 1].isInRunning:
					ballot.owner += 1
				try:
					self.list_candidates[ballot.votes[ballot.owner] - 1].give_ballot(ballot)
				except IndexError:
					raise Exception('Improper Input Format Error')
	
# ---------------
# Candidate class
# ---------------
class Candidate (object):
	'''
	object for candidates
	'''
	def __init__ (self, name):
		'''
		construct a candidate object with a given name and no ballots yet
		'''
		self.name = name
		self.ballots = []
		self.isInRunning = True
		self.isWinner = False
	
	def __repr__ (self):
		'''
		represent method allows visualization of data processing
		included for debugging purposes
		'''		
		return ('Candidate: ' + self.name + '. Ballots: ' + str(self.count_ballots()) + '. This candidate is ' + (int(not self.isInRunning) * 'not ') + 'in the running.')

	def give_ballot (self, ballot):
		'''
		adds a ballot to candidate's list of ballots
		'''
		self.ballots.append(ballot)

	def take_ballot (self, ballot):
		'''
		removes a ballot from a candidate's list of ballots
		'''
		self.ballots.remove(ballot)

	def count_ballots (self):
		'''
		returns the candidate's total number of ballots
		'''
		return len(self.ballots)

# ------------
# Ballot class
# ------------
class Ballot (object):
	'''
	object for ballots
	'''
	def __init__ (self, preferences):
		'''
		construct a ballot object out of a line containing voting preferences
		sets an index to the first preference
		'''
		self.votes = tuple(preferences)
		self.owner = 0
	
	def __repr__  (self):
		'''
		represent method allows visualization of data processing
		included for debugging purposes
		'''
		return ('Ballot: ' + str(self.votes) + '\nCurrent owner: ' + str(self.votes[self.owner]) + '. Ballot position: ' + str(self.owner))

# -------------------------
# Voting_Read_File function
# -------------------------
def Voting_Read_File (reader):
	'''
	pulls lines from reader to give back to program
	'''
	for line in reader:
		yield line

# ----------------------------
# Voting_Run_Election function
# ----------------------------
def Voting_Run_Election(election):
	'''
	processes election data until a winner or tie is detected
	'''
	while not (election.hasWinner or election.hasTie):
		winner = election.look_for_winner()
		if not winner:
			tie = election.look_for_tie()
		if not (winner or tie):
			election.mark_the_losers()
			election.pass_votes()

# ---------------------
# Voting_Write function
# ---------------------
def Voting_Write(writer, elections):
	'''
	sends output from a list of elections to a writer
	'''
	for election in elections: 
		for candidate in election.winner:
			if election == elections[-1]: 
				writer.write(candidate)
				writer.write("\n") 
			else:
				writer.write(candidate)
				writer.write('\n')
		else: 
			if elections.index(election) < len(elections): 
				writer.write('\n')
	
	
# ---------------------
# Voting_Solve function
# ---------------------
def Voting_Solve(aReader,aWriter):
	'''
	takes a reader and a writer
	extracts election information
	controls program
	'''

	line = Voting_Read_File(aReader)
	reached_EOF = False
	number_of_elections = None
	index_election = -1
	while not reached_EOF:
		try:
			render_line = next(line).strip()
		except StopIteration:
			reached_EOF = True
			continue
		if render_line == '':
			if -1 < index_election < number_of_elections:
				Voting_Run_Election(list_elections[index_election])
			index_election += 1
		elif render_line.isdigit():
			if not number_of_elections:
				number_of_elections = int(render_line)
				list_elections = [Election() for i in range(number_of_elections)]
			else:
				list_elections[index_election].number_of_candidates = int(render_line)
		elif render_line[-1].isdigit():
			try:
				rerender_line = [int(t) for t in render_line.split()]
				ballotize = Ballot(rerender_line)
				list_elections[index_election].add_ballot(ballotize)
			except ValueError: list_elections[index_election].add_candidate(Candidate(render_line))
		else:
			list_elections[index_election].add_candidate(Candidate(render_line))
	else:
		try:
			Voting_Run_Election(list_elections[index_election])
		except IndexError:
			raise Exception('Improper Input Format Error')
	Voting_Write(aWriter, list_elections)
