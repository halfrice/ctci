# Rotate Matrix
# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
# write a method to rotate the image by 90 degrees. Can you do this in place?

def rotate_matrix(m):
  for x in range(len(m)//2+1):
    for y in range(x, len(m[x])-1-x):
      # temporarily store top value
      temp = m[x][y]
      # swap top with left
      m[x][y] = m[len(m[x])-1-y][x]
      # swap left with bottom
      m[len(m[x])-1-y][x] = m[len(m[x])-1-x][len(m[x])-1-y]
      # swap bottom with right
      m[len(m[x])-1-x][len(m[x])-1-y] = m[y][len(m[x])-1-x]
      # swap right with temp
      m[y][len(m[x])-1-x] = temp
  return m
