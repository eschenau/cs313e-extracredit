#!c:\python33\python

# -------------------------------
# 
# -------------------------------

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Voting import *

# ----------
# TestVoting
# ----------
class TestVoting (TestCase) :
	# ------------
	# Ballot Class
	# ------------
	def test_Ballot_init_1 (self):
		b = Ballot([1, 2, 3])
		assert b.votes[b.owner] == 1
		b.owner += 1
		assert b.votes[b.owner] == 2
		b.owner += 1
		assert b.votes[b.owner] == 3
	
	def test_Ballot_init_2 (self):
		self.assertRaises(TypeError, Ballot, 1, 2, 3)
	
	def test_Ballot_init_3 (self):
		self.assertRaises(TypeError, Ballot, 1)
	
	def test_Ballot_init_4 (self):
		b = Ballot([1])
		self.assertEqual(b.votes[b.owner], 1)

	def test_Ballot_repr_1 (self):
		b = Ballot([1,2,3])
		w = StringIO()
		w.write(str(b))
		wout = 'Ballot: (1, 2, 3)\nCurrent owner: 1. Ballot position: 0'
		self.assertEqual(w.getvalue(),wout)

	# ---------------
	# Candidate Class
	# ---------------
	def test_Candidate_init_1 (self): 
		c = Candidate('CL4P-TP')
		assert c.name == 'CL4P-TP'
		assert not c.ballots
		assert c.isInRunning
		assert not c.isWinner

	def test_Candidate_repr_1 (self):
		c = Candidate('Handsome Jack')
		w = StringIO()
		w.write(str(c))
		wout = 'Candidate: Handsome Jack. Ballots: 0. This candidate is in the running.'
		self.assertEqual(w.getvalue(), wout)
	
	def test_Candidate_give_ballot_1 (self):
		c = Candidate('CL4P-TP')
		assert not c.ballots
	
	def test_Candidate_give_ballot_2 (self):
		c = Candidate('CL4P-TP')
		assert not c.ballots
		b = Ballot ([1, 2, 3])
		c.give_ballot(b)
		assert c.ballots
	
	def test_Candidate_take_ballot_1 (self):
		c = Candidate('CL4P-TP')
		b = Ballot ([1, 2, 3])
		c.give_ballot(b)
		assert c.ballots
		c.take_ballot(b)
		assert not c.ballots

	def test_Candidate_count_ballots_1 (self):
		c = Candidate('CL4P-TP')
		b = Ballot ([1, 2, 3])
		self.assertEqual(c.count_ballots(), 0)
	
	def test_Candidate_count_ballots_2 (self):
		c = Candidate('CL4P-TP')
		b = Ballot ([1, 2, 3])
		assert c.count_ballots() == 0
		for i in range(3):
			c.give_ballot(b)
		self.assertEqual(c.count_ballots(), 3)
	
	def test_Candidate_count_ballots_3 (self):
		c = Candidate('CL4P-TP')
		b = Ballot ([1, 2, 3])
		assert c.count_ballots() == 0
		for i in range(3):
			c.give_ballot(b)
		assert c.count_ballots() == 3
		c.take_ballot(b)
		self.assertEqual(c.count_ballots(), 2)

	# --------------
	# Election Class
	# --------------
	def test_Election_init_1 (self):
		e = Election()
		assert not e.list_candidates
		assert not e.list_ballots
		assert not e.hasWinner
		assert not e.hasTie
		assert not e.winner

	def test_Election_repr_1 (self):
		e = Election()
		e.add_candidate(Candidate('Handsome Jack'))
		e.add_ballot(Ballot([1]))
		w = StringIO()
		w.write(str(e))
		wout = 'Candidates:\nHandsome Jack  Ballots: 1, and is in the running.\n\nThere is not a winner.\n[]'
		self.assertEqual(w.getvalue(), wout)
	
	def test_Election_add_candidate_1 (self):
		e = Election()
		c = Candidate('CL4P-TP')
		e.add_candidate(c)
		assert e.list_candidates

	def test_Election_add_ballot_1 (self):
		e = Election()
		c = Candidate('CL4P-TP')
		e.add_candidate(c)
		b = Ballot ([1, 2])
		e.add_ballot(b)
		self.assertEqual(len(e.list_ballots),1)
	
	def test_Election_add_ballot_2 (self):
		e = Election()
		e.add_candidate(Candidate('Scooter'))
		b = Ballot([1, 2])
		e.add_ballot(b)
		self.assertEqual(len(e.list_candidates[0].ballots), 1)

	def test_Election_look_for_winner_1 (self): 
		e = Election()
		c = Candidate('CL4P-TP')
		e.add_candidate(c)
		b = Ballot ([1, 2])
		e.add_ballot(b)
		assert e.look_for_winner()
	
	def test_Election_look_for_winner_2 (self):
		e = Election()
		c1 = Candidate('CL4P-TP')
		c2 = Candidate('Hyperion')
		e.add_candidate(c1)
		e.add_candidate(c2)
		b1 = Ballot ([1, 2])
		b2 = Ballot ([2, 1])
		e.add_ballot(b1)
		e.add_ballot(b2)
		assert not e.look_for_winner()
	
	def test_Election_look_for_winner_3 (self):
		e = Election()
		e.add_candidate(Candidate('CL4P-TP'))
		e.add_candidate(Candidate('Handsome Jack'))
		for t in range(3):
			e.add_ballot(Ballot([1, 2]))
		assert e.look_for_winner()

	def test_Election_look_for_tie_1 (self): 
		e = Election()
		c1 = Candidate('CL4P-TP')
		c2 = Candidate('Hyperion')
		e.add_candidate(c1)
		e.add_candidate(c2)
		b1 = Ballot ([1, 2])
		b2 = Ballot ([2, 1])
		e.add_ballot(b1)
		e.add_ballot(b2)
		assert e.look_for_tie()

	def test_Election_look_for_tie_2 (self): 
		e = Election()
		c1 = Candidate('CL4P-TP')
		c2 = Candidate('Hyperion')
		e.add_candidate(c1)
		e.add_candidate(c2)
		b1 = Ballot ([1, 2])
		b2 = Ballot ([1, 2])
		e.add_ballot(b1)
		e.add_ballot(b2)
		assert not e.look_for_tie()

	def test_Election_mark_the_losers_1 (self):
		e = Election()
		for c in ['CL4P-TP', 'Hyperion', 'Handsome Jack']:
			e.add_candidate(Candidate(c))
		for b in [[1, 3, 2], [2, 3, 1], [2, 3, 1], [3, 1, 2], [3, 1, 2]]:
			e.add_ballot(Ballot(b))
		e.mark_the_losers()
		assert not e.list_candidates[0].isInRunning
	
	def test_Election_mark_the_losers_2 (self):
		e = Election()
		for c in ['CL4P-TP', 'Hyperion', 'Handsome Jack']:
			e.add_candidate(Candidate(c))
		for b in [[1, 3, 2], [2, 3, 1], [3, 1, 2], [3, 1, 2], [3, 1, 2]]:
			e.add_ballot(Ballot(b))
		e.mark_the_losers()
		assert not e.list_candidates[0].isInRunning
		assert not e.list_candidates[1].isInRunning
	
	def test_Election_pass_votes_1 (self):
		e = Election()
		for c in ['CL4P-TP', 'Hyperion', 'Handsome Jack']:
			e.add_candidate(Candidate(c))
		for b in [[1, 3, 2], [2, 3, 1], [2, 3, 1], [3, 1, 2], [3, 1, 2]]:
			e.add_ballot(Ballot(b))
		e.mark_the_losers()
		e.pass_votes()
		self.assertEqual([t.count_ballots() for t in e.list_candidates], [0, 2, 3])
	
	def test_Election_pass_votes_2 (self):
		e = Election()
		for c in ['CL4P-TP', 'Hyperion', 'Handsome Jack']:
			e.add_candidate(Candidate(c))
		for b in [[1, 3, 2], [2, 3, 1], [3, 1, 2], [3, 1, 2], [3, 1, 2]]:
			e.add_ballot(Ballot(b))
		e.mark_the_losers()
		e.pass_votes()
		self.assertEqual([t.count_ballots() for t in e.list_candidates], [0, 0, 5])

		#length of ballot.votes < number of candidates
		#ballot.votes contains improper preference

	# -------------------------
	# Voting_Read_File function
	# -------------------------
	def test_Voting_Read_File_1 (self):
		f = StringIO('1\n\n4\nRoland\nMordecai\nBrick\nLilith\n1 2 3 4\n1 3 2 4\n2 4 3 1\n2 4 3 1\n2 4 3 1\n3 4 2 1\n3 4 2 1\n3 4 2 1\n4 3 2 1\n4 3 2 1\n4 3 2 1\n4 3 2 1\n4 3 2 1')
		l = Voting_Read_File(f)
		n = next(l).strip()
		assert n.isdigit()
		n = next(l).strip()
		assert not n
		n = next(l).strip()
		assert n.isdigit()
		n = next(l).strip()
		assert n.isalpha()
	
	# ----------------------------
	# Voting_Run_Election function
	# ----------------------------
	def test_Voting_Run_Election_1 (self):
		e = Election()
		for c in ['CL4P-TP', 'Hyperion', 'Handsome Jack']:
			e.add_candidate(Candidate(c))
		for b in [[1, 3, 2], [2, 3, 1], [2, 3, 1], [3, 1, 2], [3, 1, 2]]:
			e.add_ballot(Ballot(b))
		Voting_Run_Election(e)
		assert e.hasWinner
		self.assertEqual(e.winner, ['Handsome Jack'])

	def test_Voting_Run_Election_2 (self):
		e = Election()
		for c in ['Roland', 'Mordecai', 'Brick', 'Lilith']:
			e.add_candidate(Candidate(c))
		for b in []:
			e.add_ballot(Ballot(b))
		Voting_Run_Election(e)
		assert e.hasTie
		self.assertEqual(e.winner, ['Roland', 'Mordecai', 'Brick', 'Lilith'])
	
	def test_Voting_Run_Election_3 (self):
		e = Election()
		for c in ['Axton', 'Maya', 'Salvador', 'Zer0']:
			e.add_candidate(Candidate(c))
		for b in [[2, 3, 4, 1],[2, 3, 4, 1],[2, 3, 4, 1],[2, 3, 4, 1],[2, 3, 4, 1],[2, 3, 4, 1],[4, 2, 3, 1],[4, 2, 3, 1],[4, 2, 3, 1],[4, 2, 3, 1],[3, 4, 2, 1],[3, 2, 4, 1],[1, 3, 4, 2]]:
			e.add_ballot(Ballot(b))
		Voting_Run_Election(e)
		assert e.hasWinner
		self.assertEqual(e.winner, ['Maya'])

	def test_Voting_Run_Election_4 (self):
		e = Election()
		for c in ['Gaige', 'KRIEG!']:
			e.add_candidate(Candidate(c))
		for b in [[1, 2], [2, 1], [1, 2]]:
			e.add_ballot(Ballot(b))
		Voting_Run_Election(e)
		assert e.hasWinner
		self.assertEqual(e.winner, ['Gaige'])

	def test_Voting_Run_Election_5 (self):
		e = Election()
		for c in ['Athena', 'Wilhelm', 'Nisha', 'Claptrap']:
			e.add_candidate(Candidate(c))
		for b in [[2, 4, 3, 1], [3, 4, 1, 2], [1, 4, 2, 3], [4, 3, 2, 1], [4, 1, 2, 3]]:
			e.add_ballot(Ballot(b))
		Voting_Run_Election(e)
		assert e.hasWinner
		self.assertEqual(e.winner, ['Claptrap'])
	
	def test_Voting_Run_Election_6 (self):
		e = Election()
		for c in []:
			e.add_candidate(Candidate(c))
		for b in []:
			e.add_ballot(Ballot(b))
		Voting_Run_Election(e)
		assert e.hasTie
		self.assertEqual(e.winner, ['',''])

	# ---------------------
	# Voting_Write function
	# ---------------------
	
	def test_Voting_Write_1 (self):
		e = Election()
		for c in ['Roland', 'Mordecai', 'Brick', 'Lilith']:
			e.add_candidate(Candidate(c))
		for b in [[1, 2, 3, 4],[1, 3, 2, 4],[2, 4, 3, 1],[2, 4, 3, 1],[2, 4, 3, 1],[3, 4, 2, 1],[3, 4, 2, 1],[3, 4, 2, 1],[4, 3, 2, 1],[4, 3, 2, 1],[4, 3, 2, 1],[4, 3, 2, 1],[4, 3, 2, 1]]:
			e.add_ballot(Ballot(b))
		Voting_Run_Election(e)
		w = StringIO()
		Voting_Write(w, [e])
		self.assertEqual(w.getvalue(),'Lilith\n\n')
	
	def test_Voting_Write_2 (self):
		e = Election()
		for c in ['Athena', 'Wilhelm', 'Nisha', 'Claptrap']:
			e.add_candidate(Candidate(c))
		for b in [[1,2,3,4],[2,3,4,1],[3,4,1,2],[4,1,2,3]]:
			e.add_ballot(Ballot(b))
		Voting_Run_Election(e)
		w = StringIO()
		Voting_Write(w, [e])
		self.assertEqual(w.getvalue(),'Athena\nWilhelm\nNisha\nClaptrap\n\n')
	
	def test_Voting_Write_3 (self):
		e = [Election(),Election()]
		for c in ['Handsome Jack']:
			e[0].add_candidate(Candidate(c))
		for c in ['Gaige','KRIEG!']:
			e[1].add_candidate(Candidate(c))
		for b in [[1],[1],[1]]:
			e[0].add_ballot(Ballot(b))
		for b in [[1, 2], [2, 1], [1, 2]]:
			e[1].add_ballot(Ballot(b))
		for te in e:
			Voting_Run_Election(te)
		w = StringIO()
		Voting_Write(w, e)
		self.assertEqual(w.getvalue(), 'Handsome Jack\n\nGaige\n\n')
	
	def test_Voting_Write_4 (self):
		e = [Election(),Election(),Election()]
		for c in ['Handsome Jack']:
			e[0].add_candidate(Candidate(c))
		for c in ['Gaige','KRIEG!']:
			e[1].add_candidate(Candidate(c))
		for c in ['Skag','Bullymong','Rakk']:
			e[2].add_candidate(Candidate(c))
		for b in [[1],[1],[1]]:
			e[0].add_ballot(Ballot(b))
		for b in [[1, 2], [2, 1]]:
			e[1].add_ballot(Ballot(b))
		for b in [[2, 1, 3], [3, 1, 2], [1, 3, 2], [2, 3, 1]]:
			e[2].add_ballot(Ballot(b))
		for te in e:
			Voting_Run_Election(te)
		w = StringIO()
		Voting_Write(w, e)
		self.assertEqual(w.getvalue(), 'Handsome Jack\n\nGaige\nKRIEG!\n\nBullymong\n\n')
	
	# --------------------
	# Voting_Solve function
	# --------------------
	
	def test_Voting_Solve_1 (self):
		r = StringIO('1\n\n4\nRoland\nMordecai\nBrick\nLilith\n1 2 3 4\n1 3 2 4\n2 4 3 1\n2 4 3 1\n2 4 3 1\n3 4 2 1\n3 4 2 1\n3 4 2 1\n4 3 2 1\n4 3 2 1\n4 3 2 1\n4 3 2 1\n4 3 2 1\n')
		w = StringIO()
		Voting_Solve(r,w)
		self.assertEqual(w.getvalue(),'Lilith\n\n')
	
	def test_Voting_Solve_2 (self):
		r = StringIO('1\n\n1\nCL4P-TP\n1\n1\n1\n')
		w = StringIO()
		Voting_Solve(r,w)
		self.assertEqual(w.getvalue(),'CL4P-TP\n\n')
	
	def test_Voting_Solve_3 (self):
		r = StringIO('1\n\n4\nAthena\nWilhelm\nNisha\nClaptrap\n')
		w = StringIO()
		Voting_Solve(r,w)
		self.assertEqual(w.getvalue(),'Athena\nWilhelm\nNisha\nClaptrap\n\n')
	
	def test_Voting_Solve_4 (self):
		r = StringIO('2\n\n1\nCL4P-TP\n1\n1\n1\n\n2\nGaige\nKRIEG!\n2 1\n1 2\n2 1\n1 2\n2 1\n')
		w = StringIO()
		Voting_Solve(r,w)
		self.assertEqual(w.getvalue(),'CL4P-TP\n\nKRIEG!\n\n')
	
	def test_Voting_Solve_5 (self):
		r = StringIO('1\n\n4\nAxton\nMaya\nSalvador\nZer0\n2 1 4 3\n1 2 4 3\n2 3 4 1\n1 4 3 2\n')
		w = StringIO()
		Voting_Solve(r,w)
		self.assertEqual(w.getvalue(),'Axton\nMaya\n\n')
		
	def test_Voting_Solve_6 (self):
		r = StringIO('2\n\n4\nAxton\nMaya\nSalvador\nZer0\n2 1 4 3\n1 2 4 3\n2 3 4 1\n1 4 3 2\n\n4\nRoland\nMordecai\nBrick\nLilith\n1 2 3 4\n1 3 2 4\n2 4 3 1\n2 4 3 1\n2 4 3 1\n3 4 2 1\n3 4 2 1\n3 4 2 1\n4 3 2 1\n4 3 2 1\n4 3 2 1\n4 3 2 1\n4 3 2 1\n')
		w = StringIO()
		Voting_Solve(r,w)
		self.assertEqual(w.getvalue(),'Axton\nMaya\n\nLilith\n\n')
	
	def test_Voting_Solve_7 (self):
		r = StringIO('3\n\n4\nAxton\nMaya\nSalvador\nZer0\n2 1 4 3\n1 2 4 3\n2 3 4 1\n1 4 3 2\n\n4\nRoland\nMordecai\nBrick\nLilith\n1 2 3 4\n1 3 2 4\n2 4 3 1\n2 4 3 1\n2 4 3 1\n3 4 2 1\n3 4 2 1\n3 4 2 1\n4 3 2 1\n4 3 2 1\n4 3 2 1\n4 3 2 1\n4 3 2 1\n\n1\nCL4P-TP\n1\n1\n1\n')
		w = StringIO()
		Voting_Solve(r,w)
		self.assertEqual(w.getvalue(),'Axton\nMaya\n\nLilith\n\nCL4P-TP\n\n')
	
	def test_Voting_Solve_8 (self):
		r = StringIO('1\n\n2\nAxton\nMaya\n2 1\n\n2\nSalvador\nZer0\n2 1\n')
		w = StringIO()
		self.assertRaises(Exception, Voting_Solve, r, w)

# ----
# main
# ----

main()

'''
16 functions tested
43 total tests
need 48 tests total
need 5 more tests

coverage3 run --branch TestVoting.py
coverage3 report -m
'''
