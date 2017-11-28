from src.c1.string_compression import *

def test_string_compression():
  assert string_compression('aabcccccaaa') == 'a2b1c5a3'
  assert string_compression('abcd') == 'abcd'
  assert string_compression('abbcccdddda') == 'a1b2c3d4a1'
  assert string_compression('LLLLlllmmmaaoooo') == 'L4l3m3a2o4'
