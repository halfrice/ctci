# Check Permutation

# Given two strings, write a method to decide if one is a permutation of the other.

def check_permutation(s1, s2):
  if len(s1) != len(s2):
    return False
  su = 0
  for i in range(len(s1)):
    su += ord(s1[i])-ord(s2[i])
  return su == 0
