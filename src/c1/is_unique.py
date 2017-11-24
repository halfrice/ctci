# Is Unique

# Implement an algorithm to determine if a string has all unique characters. What if you cannot
# use additional data structures?

def is_unique(string):
  hash_table = {}
  for letter in string:
    if letter in hash_table:
      return False
    hash_table[letter] = True
  return True

def is_unique_no_data_structures(string):
  s = sorted(string)
  for i in range(1, len(s)):
    if s[i-1] == s[i] and ord(s[i-1]) == ord(s[i]):
      return False
  return True
