from src.c1.zero_matrix import *

def test_zero_matrix():
  assert zero_matrix([[1, 0, 3], [4, 5, 6], [7, 8, 9]]) == [[0, 0, 0], [4, 0, 6], [7, 0, 9]]