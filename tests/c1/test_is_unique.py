from src.c1.is_unique import *

def test_is_unique():
  assert is_unique('lmao') == True
  assert is_unique('roflgg') == False

def test_is_unique_no_data_structures():
  assert is_unique_no_data_structures('abcdefg') == True
  assert is_unique_no_data_structures('abcdefgg') == False
