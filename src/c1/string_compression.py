# String Compression

# Implement a method to perform basic string compression using the counts of repeated characters.
# For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not
# become smaller than the original string, your method should return the original string. You
# can assume the string has only uppercase and lowercase letters (a-z).

def string_compression(s):
  r = ''
  count = 1
  for i in range(len(s)):
    cur = s[i]
    next = s[i+1] if i+1 < len(s) else None
    if next and cur == next:
      count += 1
    else:
      r += cur+str(count)
      count = 1
  if len(r) > len(s):
    return s
  return r
