# Palindrome Permutation
# Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is
# a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of
# letters. The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input:    Tact Coa
# Output:   True (permutations: "taco cat", "atco, cta", etc.)

import collections

def palindrome_permutation(string):
  s = ''.join(string.lower().split())
  freq_table = collections.Counter(s).values()
  is_palindrome = sum(e % 2 for e in freq_table) < 2
  return is_palindrome
