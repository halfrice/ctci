from src.c1.check_permutation import *

def test_check_permutation():
  assert check_permutation('lmao', 'maol') == True
  assert check_permutation('wtfbro', 'nahman') == False