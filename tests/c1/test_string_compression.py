from src.c1.string_compression import *

def test_string_compression():
  assert string_compression('aabcccccaaa') == 'a2b1c5a3'
