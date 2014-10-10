#ExtraCredit.py

class Deque: 
	def __init__(self):
		self.d_list=[]
	def add_front(self, item): 
		self.d_list.insert(0, item)
	def add_back (self, item): 
		self.d_list.append(item)
	def remove_front (self):
		self.d_list.pop(0)
	def remove_back(self): 
		self.d_list.pop()
	def in_deque(self, item): 
		if item in self.d_list:
			return self.d_list.index(item)
		else:
			return False
	def is_empty(self):
		return len(self.d_list) == 0
	def size (self):
		return len(self.d_list)
	def print_deque(self):
		for items in self.d_list:
			print ("%s" %(items), end=" ")
	def is_last (self, item):
		return self.d_list[-1]==item
	def get_last (self):
		return self.d_list [-1]


#------TESTING DEQUE--------------------
d = Deque()
d.add_front(1)
d.add_front(2)
d.add_back(7)
d.print_deque()

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
		TASK = TAKE FIRST NUMBER as Task
		FOLLOW = TAKE LAST NUMBER IN LINE LIST AS TASK IT MUST FOLLOW
		>> might be a conflict when ordering non-dependent tasks(LOOK AT SPOJ)
			IF TASK tries to occupy same space in deque: 
				take the lower one but add the higher task after lower
				IF DEQUE.is_last ! TRUE for the FOLLOW for the TASK: 
					COMPARE DEQUE.getlast to TASK: 
						if TASK > DEQUE.getlast: 
							deque.add_back(task)
						else: 
							add before the deque.getlast



def getFile(r,w):
	for rows in r: 
		rows = rows.strip()
		rows = rows.split (" ")
		yield rows
def analyzeRows(rows): 
	task = rows[0]
	num_depend = rows[1]
	dependants = rows [2:2+int(num_depend)+1]
	print ("Task: %s, k: %s, Before Task: %s" %(task, num_depend, dependants))

def EC_solve(r,w):
	class Node: 
		def __init__(self, init_data): 
			self.data = init_data
			self.next = None
		def get_data (self): 
			return self.data
		def get_next (self):
			return self.next
		def set_data(self,new_data): 
			self.data = new_data
		def set_next (self, new_next):
			self.set_next = new_next
	class UnordereredList: 
		def __init__(self):
			self.head = None
		def add(self, item): 
			temp = Node(item)
			temp.set_next(self.head)
			self.head = temp

	task_list = UnordereredList()
	
	for rows in getFile(r,w):
		edited_rows=analyzeRows(rows)
		print (edited_rows)
"""


def main():
	main()
