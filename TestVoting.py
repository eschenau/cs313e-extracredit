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
		pass
	
	def test_Candidate_give_ballot_1 (self):
		pass
	
	def test_Candidate_take_ballot_1 (self):
		pass

	def test_Candidate_count_ballots_ 1 (self):
		pass

	# --------------
	# Election Class
	# --------------
	
	def test_Election_init_1 (self):
		pass
	
	def test_Election_add_candidate_1 (self):
		pass

	def test_Election_add_ballot_1 (self):
		pass

	def test_Election_look_for_winner_1 (self):
		pass
	
	def test_Election_look_for_tie_1 (self):
		pass
	
	def test_Election_mark_the_losers_1 (self):
		pass
	
	def test_Election_pass_votes_1 (self):
		pass
	
	# ------------------
	# Voting_Read_File function
	# ------------------
	
	def test_Voting_Read_File_1 (self):
		pass
	
	# --------------------
	# Voting_Run_Election function
	# --------------------
	
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
