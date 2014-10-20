#!/usr/bin/env/python3
#Esther Schenau, Cameron Miller
#-----Collection of Lists-------

list_lines = []

#-------------------------------


def ReadFile (r, w): 
	
	for lines in r: 
		lines = lines.strip() 
		list_lines.append(lines)
	
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
			if loi == "" and list_lines: 
				index_election+=1

				print ("Election Number:", index_election)
				list_lines.pop(0)
				number_candidates = int (list_lines.pop(0))
				print ("NUMBER CAND:", number_candidates)

				for i in range (0, number_candidates):
					list_elections[index_election].add_candidate(Candidate(list_lines.pop(0)))

				try: 
					while list_lines[0] != "": 

						temp = list_lines[0].strip()
						temp = list_lines[0].split()
						temp = [int (t) for t in temp]
						t = Ballot(temp) 
						list_elections[index_election].add_ballot(t.init_owner(list_elections[index_election].return_Candidates()))
						list_lines.pop(0)
				
				except IndexError: 
					pass
				#----Troubleshooting loop------------------------------

				
				for candidate in list_elections[index_election].list_candidates:
					print ("Name:", candidate.name, end = " ")
					print (candidate.count_ballots())	

				#------------------------------------------------------
class Election(object): 

	def __init__(self):
		self.list_candidates = []
		self.list_ballots = []
		self.hasWinner = False
		self.hasTie = False

	def add_candidate(self, candidate):
		self.list_candidates.append(candidate)

	def add_ballot(self, ballot):
		self.list_ballots.append(ballot)
	def return_Candidates(self): 
		return self.list_candidates

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
		#self.owner = 0
	def init_owner (self, list_candidates): 
		list_candidates[self.votes[0] - 1].give_ballot(self)

	def show_ballot (self): 
		print (self.votes)



