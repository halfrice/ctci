# URLify

# Write a method to replace all spaces in a string with "%20". You may assume the string has
# sufficient space at the end to hold the additional characters, and that you are given the
# "true" length of the string.
# e.g.
# Input:    'Mr. John Smith    ', 13
# output:   'Mr.%20John%20Smith'

def urlify(string, true_len):
  s = ''
  for i in range(true_len+1):
    if string[i] == ' ' and ord(string[i]) == 32:
      s += '%20'
    else:
      s += string[i]
  return s

def urlify_swap_in_place(string, true_len):
  s = list(string)
  wedge = '%20'[::-1]
  offset = len(s)-true_len-1
  start_index = len(s)-offset-1
  for i in range(start_index, -1, -1):
    if s[i] != ' ':
      s[i+offset] = s[i]
    if s[i] == ' ':
      # wedge
      for j in range(len(wedge)):
        s[i+offset-j] = wedge[j]
      offset -= 2
  return s
