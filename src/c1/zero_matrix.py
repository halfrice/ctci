# Zero Matrix

# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are
# set to 0.

def zero_matrix(m):
  zero_coords = []
  for row in range(len(m)):
    for col in range(len(m[row])):
      if m[row][col] == 0:
        zero_coords.append([row, col])
  for pos in zero_coords:
    x = pos[0]
    y = pos[1]
    for i in range(len(m)):
      if i == x:
        for j in range(len(m[i])):
          if m[x][j] != 0:
            m[x][j] = 0
      if m[i][y] != 0:
        m[i][y] = 0
  return m
