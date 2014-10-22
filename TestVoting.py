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

	'''
	# -------------
	# netflix_write
	# -------------

	def test_netflix_write (self):
		w = StringIO()
		netflix_write(w, ['1.2'])
		self.assertEqual(w.getvalue(), '1.2')

	# ---------------------------
	# get netflix_make_prediction
	# ---------------------------

	def test_netflix_make_prediction_1 (self):
		uI, mI = 1, 1
		uDC = {1 : [1,1]}
		mDC = {1 : [1,1],'overallAverageRating' : 1}
		p = netflix_make_prediction(uI, uDC, mI, mDC)
		self.assertEqual(p,1)

	def test_netflix_make_prediction_2 (self):
		uI, mI = 1, 1
		uDC = {1 : [1,1]}
		mDC = {1 : [5,5],'overallAverageRating' : 1}
		p = netflix_make_prediction(uI, uDC, mI, mDC)
		self.assertGreater(p,2.236)
		self.assertLess(p,2.237)

	def test_netflix_make_prediction_3 (self):
		uI, mI = 1, 1
		uDC = {1 : [1,5]}
		mDC = {1 : [1,5],'overallAverageRating' : 1}
		p = netflix_make_prediction(uI, uDC, mI, mDC)
		self.assertGreater(p,1.495)
		self.assertLess(p,1.496)

	def test_netflix_make_prediction_4 (self):
		uI, mI = 1, 1
		uDC = {1 : [5,1]}
		mDC = {1 : [5,1],'overallAverageRating' : 1}
		p = netflix_make_prediction(uI, uDC, mI, mDC)
		self.assertGreater(p,3.343)
		self.assertLess(p,3.344)

	def test_netflix_make_prediction_5 (self):
		uI, mI = 1, 1
		uDC = {1 : [2.5,3]}
		mDC = {1 : [2.5,3],'overallAverageRating' : 3}
		p = netflix_make_prediction(uI, uDC, mI, mDC)
		self.assertGreater(p,2.616)
		self.assertLess(p,2.617)

	def test_netflix_make_prediction_6 (self):
		uI, mI = 0, 1
		uDC = {1 : [1,1]}
		mDC = {1 : [1,1],'overallAverageRating' : 1}
		self.assertRaises(AssertionError, netflix_make_prediction, uI, uDC, mI, mDC)

	def test_netflix_make_prediction_7 (self):
		uI, mI = 1, 0
		uDC = {1 : [1,1]}
		mDC = {1 : [1,1],'overallAverageRating' : 1}
		self.assertRaises(AssertionError, netflix_make_prediction, uI, uDC, mI, mDC)

	# --------------------
	# netflix_compute_rmse
	# --------------------

	def test_netflix_compute_rmse_1 (self):
		aR, pR = [1], [1]
		r = netflix_compute_rmse(aR, pR)
		self.assertEqual(r, 0)

	def test_netflix_compute_rmse_2 (self):
		aR, pR = [1,2], [2,1]
		r = netflix_compute_rmse(aR, pR)
		self.assertEqual(r, 1)

	def test_netflix_compute_rmse_3 (self):
		aR, pR = [1,3,1], [3,1,3]
		r = netflix_compute_rmse(aR, pR)
		self.assertEqual(r, 2)

	def test_netflix_compute_rmse_4 (self):
		aR, pR = [1,4,4,1], [4,1,1,4]
		r = netflix_compute_rmse(aR, pR)
		self.assertEqual(r, 3)

	def test_netflix_compute_rmse_5 (self):
		aR, pR = [1,1,1,1,1], [5,5,5,5,5]
		r = netflix_compute_rmse(aR, pR)
		self.assertEqual(r, 4)

	def test_netflix_compute_rmse_6 (self):
		aR, pR = [1,2,3,4,5], [5,5,5,5,5]
		r = netflix_compute_rmse(aR, pR)
		self.assertGreater(r, 2.449)
		self.assertLess(r, 2.450)

	def test_netflix_compute_rmse_7 (self):
		aR, pR = [1], [1, 2]
		self.assertRaises(AssertionError, netflix_compute_rmse, aR, pR)

	def test_netflix_compute_rmse_8 (self):
		aR, pR = [1, 2], [1]
		self.assertRaises(AssertionError, netflix_compute_rmse, aR, pR)

	# ----------------------
	# netflix_withouta_prize
	# ----------------------
		
	def test_netflix_withouta_prize_1 (self):
		r = StringIO('1:\n30878\n10:\n1952305\n1000:\n2326571\n')
		w = StringIO()
		netflix_withouta_prize(r,w)
		self.assertEqual(w.getvalue(), 'rating\n1.0 - 5.0\n...\n1:\n3.8\n...\n10:\n3.2\n...\n1000:\n3.6\n...\nRMSE: 0.37 \n3 records total')

	def test_netflix_withouta_prize_2 (self):
		r = StringIO('')
		w = StringIO()
		netflix_withouta_prize(r,w)
		self.assertEqual(w.getvalue(), 'rating\n1.0 - 5.0\n...\nRMSE: 0.00 \n0 records total')

	def test_netflix_withouta_prize_3 (self):
		r = StringIO('1:\n')
		w = StringIO()
		netflix_withouta_prize(r,w)
		self.assertEqual(w.getvalue(), 'rating\n1.0 - 5.0\n...\n1:\n...\nRMSE: 0.00 \n0 records total')
	'''

# ----
# main
# ----

main()
