#ExtraCredit.py

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



def main():
	main()
