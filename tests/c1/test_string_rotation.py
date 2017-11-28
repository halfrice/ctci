from src.c1.string_rotation import *

def test_string_rotation():
  assert string_rotation('erbottlewat', 'waterbottle') is True
  assert string_rotation('erbottlewut', 'waterbottle') is False
