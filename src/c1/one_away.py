# One Away

# There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to
# check if they are one edit (or zero edits) away.
# EXAMPLE
# pale,  ple   -> true
# pales, pale  -> true
# pale,  bale  -> true
# pale,  bake  -> false

from collections import Counter

def one_away(s1, s2):
  if abs(len(s1)-len(s2)) > 1:
    return False
  min_s, max_s = (s1, s2) if len(s1) >= len(s2) else (s2, s1)
  freq_min = Counter(min_s)
  freq_max = Counter(max_s)
  diff = 0
  for e in freq_max:
    if e in freq_min:
      diff += abs(freq_min[e]-freq_max[e])
    else:
      diff += freq_max[e]
  return diff <= 1 and diff >= 0
