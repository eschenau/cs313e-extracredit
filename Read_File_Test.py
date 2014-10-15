#Esther Schenau, Cameron Miller


def ReadFile (r, w): 
	list_lines = []
	candidates = []
	for lines in r: 
		lines = lines.strip() 
		list_lines.append(lines)

	number_of_elections = list_lines[0]
	list_lines.pop(0)

	print (number_of_elections)
	print (list_lines)

	while len(list_lines) > 0:
		#LOI = line of interest
		for i in list_lines:
			loi = list_lines[0]
			if loi == "": 
				number_candidates = int(list_lines [1])
				print ("Number cand:", number_candidates)
				list_lines.pop(0)
				for i in range (1, number_candidates+1):
					candidates.append(list_lines[i]) 
			else: 
				#READ BALLOTS IN HERE
				list_lines.pop(0)
	print (candidates)
	print ("list lines:", list_lines)