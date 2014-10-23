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

	def test_ballot_init_1 (self):
		b = Ballot([1, 2, 3])
		assert b.votes[b.owner] == 1
		b.owner += 1
		assert b.votes[b.owner] == 2
		b.owner += 1
		assert b.votes[b.owner] == 3

	# ---------------
	# Candidate Class
	# ---------------

	def test_candidate_init_1 (self): 
		pass
	
	def test_candidate_give_ballot_1 (self):
		pass
	
	def test_candidate_take_ballot_1 (self):
		pass

	def test_candidate_count_ballots_ 1 (self):
		pass

	# --------------
	# Election Class
	# --------------
	
	def test_election_init_1 (self):
		pass
	
	def test_election_add_candidate_1 (self):
		pass

	def test_election_add_ballot_1 (self):
		pass

	def test_election_look_for_winner_1 (self):
		pass
	
	def test_election_look_for_tie_1 (self):
		pass
	
	def test_election_mark_the_losers_1 (self):
		pass
	
	def test_election_pass_votes_1 (self):
		pass
	
	# ------------------
	# read_file function
	# ------------------
	
	def test_read_file_1 (self):
		pass
	
	# --------------------
	# RunElection function
	# --------------------
	
	def test_runelection_1 (self):
		pass
	
	# --------------------
	# VotingSolve function
	# --------------------
	
	def test_votingsolve_1 (self):
		pass

# ----
# main
# ----

main()
