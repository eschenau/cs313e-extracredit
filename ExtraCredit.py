#ExtraCredit.py
"""

Algorithm
1. Read in file, extract relevant information
>> How to ignore the first line
		>> Reading each line as a list (won't get more than 100)
			>> If LIST size == 2: 
					take first number as N tasks
>> read lines by iteration not index
	FOR LINE IN FILE: 
		STRIP 
		SPLIT AT SPACE
		if List size == 2: 
			return
		TASK = TAKE FIRST NUMBER as Task
		FOLLOW = TAKE LAST NUMBER IN LINE LIST AS TASK IT MUST FOLLOW
		>> might be a conflict when ordering non-dependent tasks(LOOK AT SPOJ)
			IF TASK tries to occupy same space in deque: 
				take the smaller task but add the higher task after lower
				IF DEQUE.is_last ! TRUE for the FOLLOW for the TASK: 
					COMPARE DEQUE.getlast to TASK: 
						if TASK > DEQUE.getlast: 
							deque.add_back(task)
						else: 
							add before the deque.getlast


"""

def getFile(r,w):
	for rows in r: 
		rows = rows.strip()
		rows = rows.split (" ")
		yield rows
def analyzeRows(rows): 
	#range_set = set() 
	task = int(rows[0])
	num_depend = rows[1]
	task_before = rows [-1]
	#Making new dictionary
	return task,num_depend, task_before
def EC_solve(r,w):	
	task_set = set()
	dict_tasks = {} 
	for rows in getFile(r,w):
		task, num_depend, task_before= analyzeRows(rows)
		dict_tasks [task] = int(task_before)
		print ("t:", task)
		print ("b:", task_before)
	print (dict_tasks)
	for v in dict_tasks.values():
		if v not in dict_tasks.keys(): 
			start_value = v
	print ("starting point:",v) 




	"""IF A VALUE DOES NOT EXIST IN THE KEY, THAT's THE STARTING VALUE


	#at this point, data has been extracted from

"""

def main():
	main()
