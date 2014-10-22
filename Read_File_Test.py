#!/usr/bin/env/python3
#Esther Schenau, Cameron Miller
#-----Collection of Lists-------

list_lines = []


def readFile (r):
	for lines in r: 
		lines = lines.strip() 
		list_lines.append(lines)
	return list_lines
#-------------------------------

def VotingSolve(r,w):

	readFile(r)
	number_of_elections = int(list_lines[0])
	print ("Election Count:", number_of_elections)
	list_elections = [Election() for i in range (number_of_elections)] 
	index_election = -1
	list_lines.pop(0)

	#Blank line is indicator of next election 
	while len(list_lines) > 0:
		#LOI = line of interest
		for i in list_lines:
			loi = list_lines[0]
			#print (loi)
			if loi == "":# and list_lines: 
				
				if index_election > -1: 
					#PROCESS ALL THIS SHIT HERE
					#Give ballots to initial owners
					#for t in list_elections[index_election].list_ballots:
					#	list_elections[index_election].list_candidates[t.votes[t.owner]-1].give_ballot(t)
					winner = list_elections[index_election].look_for_winner()
					if not winner: tie = list_elections[index_election].look_for_tie()
					if not winner and not tie:
						list_elections[index_election].mark_the_losers()
						list_elections[index_election].pass_votes()
				print ("Ballot length in election:", len(list_elections[index_election].list_ballots))
				print ("Length of Candidate List:", len(list_elections[index_election].list_candidates))



				index_election+=1

				print ("Election Number:", index_election)
				list_lines.pop(0)
				number_candidates = int (list_lines.pop(0))
				#print ("NUMBER CAND:", number_candidates)

				for i in range (0, number_candidates):
					list_elections[index_election].add_candidate(Candidate(list_lines.pop(0)))

				try: 
					while list_lines and list_lines[0] != "": 

						temp = list_lines[0].strip()
						temp = list_lines[0].split()
						temp = [int (t) for t in temp]
						t = Ballot(temp) 
						list_elections[index_election].add_ballot(t)
						list_elections[index_election].list_candidates[t.votes[t.owner]-1].give_ballot(t)

						list_lines.pop(0)

		
				except IndexError: 
					#winner = list_elections[index_election - 1].look_for_winner()
					#if not winner: tie = list_elections[index_election - 1].look_for_tie()
					#if not winner and not tie:
					#	list_elections[index_election - 1].mark_the_losers()
					#	list_elections[index_election - 1].pass_votes()
					#----Troubleshooting loop------------------------------
				
					#for candidate in list_elections[index_election].list_candidates:
						#print ("Name:", candidate.name, end = " ")
						#print (candidate.count_ballots())	

					#------------------------------------------------------


					print ("EOF?")
	else:
		winner = list_elections[index_election].look_for_winner()
		if not winner: tie = list_elections[index_election].look_for_tie()
		if not winner and not tie:
			list_elections[index_election].mark_the_losers()
			list_elections[index_election].pass_votes()
		print ("Ballot length in election:", len(list_elections[index_election].list_ballots))
		print ("Length of Candidate List:", len(list_elections[index_election].list_candidates))
"""

Election Logic

Giving to first owner	list_elections[index_election].list_candidates[t.votes[t.owner]-1].give_ballot(t)

1. Give ballots to first owner
2. Check for winner
3. Check for tie_check
4. Mark losers
5. Pass votes of losers to the preferences
6. Repeat Steps 2-5




"""

				
class Election(object): 

	def __init__(self):
		self.list_candidates = []
		self.list_ballots = []
		self.hasWinner = False
		self.hasTie = False
		self.winner = []

	def add_candidate(self, candidate):
		self.list_candidates.append(candidate)

	def add_ballot(self, ballot):
		self.list_ballots.append(ballot)
	def return_Candidates(self): 
		return self.list_candidates
	
	def look_for_winner (self):
		if len(self.list_candidates) == 1:
			self.hasWinner = True
			self.list_candidates[0].isWinner = True
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

		print ('is there a winner?', self.hasWinner)
		print ("winner:",self.winner)
		return self.hasWinner
	
	def look_for_tie (self):
		tie_check = [self.list_candidates[0].count_ballots() == candidate.count_ballots() for candidate in self.list_candidates[1:] if candidate.isInRunning]
		theres_a_tie = True
		for check in tie_check:
			theres_a_tie = theres_a_tie and check
		if theres_a_tie:
			for candidate in self.list_candidates:
				if candidate.isInRunning:
					candidate.isWinner = True
				self.winner = [cand.name for cand in self.list_candidates if cand.isInRunning]
			print ("There's a tie.")
			print(self.winner)
		return theres_a_tie

	def mark_the_losers (self):
		loss_threshold = min(t.count_ballots() for t in self.list_candidates)
		for cand in self.list_candidates:
			if cand.count_ballots() <= loss_threshold:
				cand.isInRunning = False

	def pass_votes (self):
		losers = [t for t in self.list_candidates if not t.isInRunning]
		for non_candidate in losers:
			for ballot in non_candidate.ballots:
				while not self.list_candidates[ballot.votes[ballot.owner] - 1].isInRunning:
					#self.list_candidates[ballot.votes[ballot.owner] - 1].take_ballot(ballot)
					ballot.owner += 1
					self.list_candidates[ballot.votes[ballot.owner] - 1].give_ballot(ballot)

class Candidate (Election):
	'''
	'''
	def __init__ (self, name):
		self.name = name
		self.ballots = []#set()
		self.isInRunning = True

	def give_ballot (self, ballot):
		self.ballots.append(ballot)

	def take_ballot (self, ballot):
		self.ballots.remove(self.ballots.index(ballot))

	def count_ballots (self):
		return len(self.ballots)

class Ballot (Candidate):
	'''
	'''
	def __init__ (self, preferences):
		'''
		'''
		self.votes = tuple(preferences)
		self.owner = 0

	def init_owner (self, list_candidates): 
		list_candidates[self.votes[0] - 1].give_ballot(self)

	def show_ballot (self): 
		print (self.votes)



