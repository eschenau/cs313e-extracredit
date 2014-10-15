#!/usr/bin/env/python3
#Esther Schenau, Cameron Miller
class Ballot(object):
	def __init__(self, ballot): 
		self.ballot = tuple(ballot)
	
	

def ReadFile (r, w): 
	
	#-----Collection of Lists-------

	list_lines = []
	list_candidates = []
	list_ballots = []

	#-------------------------------
	
	for lines in r: 
		lines = lines.strip() 
		list_lines.append(lines)
	number_of_elections = int(list_lines[0])
	list_lines.pop(0)

	while len(list_lines) > 0:
		#LOI = line of interest
		for i in list_lines:
			loi = list_lines[0]
			if loi == "": 
				list_lines.pop(0)
				number_candidates = int(list_lines [0])
				list_lines.pop(0)

				for i in range (0, number_candidates):
					list_candidates.append(list_lines[0]) 
					list_lines.pop(0)

			else: 
				#READ BALLOTS IN HERE
				#make list a Ballot object
				temp = loi.split()
				temp = [int (c) for t in temp for c in t]
				list_ballots.append(temp)
				list_lines.pop(0)
	

	print ("number of elections:", number_of_elections)
	print ("Candidates:",list_candidates)
	print ("Ballots:", list_ballots)
