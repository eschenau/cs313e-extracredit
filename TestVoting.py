#!c:\python33\python

# -------------------------------
# 
# -------------------------------

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Read_File_Test import *

# -----------
# Testnetflix
# -----------

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

	# ---------------
	# Candidate Class
	# ---------------

	def test_Candidate_init_1 (self): 
		c = Candidate('CL4P-TP')
		assert c.name == 'CL4P-TP'
		assert not c.ballots
		assert c.isInRunning
		assert not c.isWinner
	
	def test_Candidate_give_ballot_1 (self):
		c = Candidate('CL4P-TP')
		b = Ballot ([1, 2, 3])
		c.give_ballot(b)
		assert c.ballots
	
	def test_Candidate_take_ballot_1 (self):
		c = Candidate('CL4P-TP')
		b = Ballot ([1, 2, 3])
		c.give_ballot(b)
		c.take_ballot(b)
		assert not c.ballots

	def test_Candidate_count_ballots_ 1 (self):
		c = Candidate('CL4P-TP')
		b = Ballot ([1, 2, 3])
		c.give_ballot(b)
		c.give_ballot(b)
		c.give_ballot(b)
		assert c.count_ballots() == 3

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
	
	def test_Election_add_candidate_1 (self):
		e = Election()
		c = Candidate('CL4P-TP')
		e.add_candidate(c)
		assert e.list_candidates

	def test_Election_add_ballot_1 (self):
		e = Election()
		b = Ballot ([1, 2])
		e.add_ballot(b)
		assert e.list_ballots

	def test_Election_look_for_winner_1 (self): 
		e = Election()
		c = Candidate('CL4P-TP')
		e.add_candidate(c)
		b = Ballot ([1, 2])
		e.add_ballot(b)
		assert e.look_for_winner
	
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
		assert not e.look_for_winner

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
		assert e.look_for_tie

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
		assert not e.look_for_tie

	def test_Election_mark_the_losers_1 (self):
		pass
	
	def test_Election_pass_votes_1 (self):
		pass
	
	# -------------------------
	# Voting_Read_File function
	# -------------------------
	
	def test_Voting_Read_File_1 (self):
		pass
	
	# ----------------------------
	# Voting_Run_Election function
	# ----------------------------
	
	def test_Voting_Run_Election_1 (self):
		pass
	
	# ---------------------
	# Voting_Write function
	# ---------------------
	
	def test_Voting_Write_1 (self):
		pass
	
	# --------------------
	# Voting_Solve function
	# --------------------
	
	def test_Voting_Solve_1 (self):
		pass

# ----
# main
# ----

main()
