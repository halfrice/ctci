from src.c1.one_away import *

def test_one_away():
  assert one_away('pale', 'ple') is True
  assert one_away('pales', 'pale') is True
  assert one_away('pale', 'bale') is True
  assert one_away('pale', 'bake') is False
  assert one_away('lmao', 'Lma0') is False
