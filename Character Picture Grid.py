grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']] 


row1 = [''.join(grid[0][0:1] + grid[1][0:4] + grid[2][0:2] + grid[0][0:2])]
row2 = [''.join(grid[1][0:3] + grid[1][1:3] + grid[2][0:3] + grid[0][0:1])]
row3 = [''.join(grid[1][0:3] + grid[1][1:3] + grid[2][0:3] + grid[0][0:1])]
row4 = [''.join(grid[0][0:2] + grid[1][1:3] + grid[2][0:3] + grid[0][0:2])]
row5 = [''.join(grid[0][0:3] + grid[1][1:2] + grid[2][0:2] + grid[0][0:3])]
row6 = [''.join(grid[0][0:4] + grid[1][1:1] + grid[2][0:1] + grid[0][0:4])]


rows = [row1, row2, row3, row4, row5, row6]


def rowAlign(rows):

 for i in rows:
  strings = [str(integer) for integer in i]
  a_strings = "".join(strings)
  print(a_strings)

rowAlign(rows)
