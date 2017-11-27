from src.c1.urlify import *

def test_urlify():
  assert urlify('Mr. John Smith    ', 13) == 'Mr.%20John%20Smith'
  assert urlify('Mr. John Smith', 13) == 'Mr.%20John%20Smith'

def test_urlify_swap_in_place():
  assert urlify_swap_in_place('Mr. John Smith    ', 13) == 'Mr.%20John%20Smith'
  assert urlify_swap_in_place('Mr.  John  Smith        ', 15) == 'Mr.%20%20John%20%20Smith'
