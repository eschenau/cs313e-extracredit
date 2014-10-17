#!/usr/bin/env/python3
#Esther Schenau, Cameron Miller
#-----Collection of Lists-------

list_lines = []
list_candidates =[]
list_ballots = []

#-------------------------------
class Election(object): 
	def __init__(self): 
		list_candidates = []
		list_ballots = [] 
	def readCandidates(self,candidate): 
		list_candidates.append()
	def readBallots(self,ballot): 
		list_ballots.append(ballot)


class Candidate (object):
	'''
	'''
	def __init__ (self, name):
		self.name = name
		self.ballots = []#set()
		self.isInRunning = True
	def name_candidate(self):
		print (self.name, end = " ")

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

def ReadFile(r,w):
	for lines in r: 
		lines = lines.strip() 
		list_lines.append(lines)
	number_of_elections = int(list_lines[0])
	list_lines.pop(0)
	#Blank line is indicator of next election 
	while len(list_lines) > 0:
		#LOI = line of interest
		for i in list_lines:
			loi = list_lines[0]
			if loi == "":
				#PROCESS OLD ELECTION
	 			new_election = Election() #START OF NEW ELECTION
				
				list_lines.pop(0)
				number_candidates = int(list_lines[0])
				list_lines.pop(0)

				for i in range (0, number_candidates):
					"""
					"""	
					list_candidates.append(Candidate(list_lines[0])) 
					#new_election.readCandidates(Candidate(list_lines[0]))
					list_lines.pop(0)
				'''while j in list_lines != "": 
					temp = loi.split()
					temp = tuple(int (c) for t in temp for c in t)
					new_election.readBallots(Ballot(temp))
					list_lines.pop(0)

				'''
			else: 
				temp = loi.split()
				temp = tuple(int (c) for t in temp for c in t)
				list_ballots.append(Ballot(temp))
				list_lines.pop(0)


	print ("Elections:", number_of_elections)
	print ("Candidates:", len(list_candidates))
	for index in list_candidates: 
		index.name_candidate()
		print (index.count_ballots())
	print ("Ballots:")
	for thing in list_ballots: 
		thing.show_ballot()

