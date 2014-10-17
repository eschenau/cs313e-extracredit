#!/usr/bin/env/python3
#Esther Schenau, Cameron Miller
#-----Collection of Lists-------

list_lines = []



list_candidates = []
list_ballots = []

#-------------------------------


def ReadFile (r, w): 
	
	for lines in r: 
		lines = lines.strip() 
		list_lines.append(lines)
	
	number_of_elections = int(list_lines[0])
	list_elections = [Election() for i in range (number_of_elections)] 
	index_election = 0
	
	list_lines.pop(0)
	
	#Blank line is indicator of next election 
	while len(list_lines) > 0:
		#LOI = line of interest
		for i in list_lines:
			loi = list_lines[0]
			#print (loi)
			if loi == "": 
				print ("ENTERED IF")
				list_lines.pop(0)
				number_candidates = int (list_lines.pop(0))
				print ("NUMBER CAND:", number_candidates)

				for i in range (0, number_candidates):
					list_elections[index_election].add_candidate(Candidate(list_lines.pop(0)))
				
				print ("Current line:", list_lines[0])
				#----Troubleshooting loop------------------------------
				for candidate in list_elections[index_election].list_candidates:
					print (candidate.name)

				#------------------------------------------------------
				while list_lines[0] != "": 
					print("Loi:", list_lines[0])  
				#READ BALLOTS IN HERE
				#make list a Ballot object
					temp = list_lines[0].strip()
					temp = list_lines[0].split()
					temp = [int (c) for t in temp for c in t]
					list_elections[index_election].add_ballot(Ballot(temp))
					list_lines.pop(0)
			index_election += 1


	"""
	print ("Elections:", number_of_elections)
	print ("Candidates:", len(list_candidates))
	print ("Ballots:", len(list_ballots))
	for index in list_candidates: 
		index.name_candidate()
		print (index.count_ballots())
	print ("Ballots:")
	for thing in list_ballots: 
		thing.show_ballot()
	"""


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
		list_candidates[self.votes[self.owner] - 1].give_ballot(self)

	def show_ballot (self): 
		print (self.votes)
