grid = [['.', '.', '.', '.', '.', '.'],
 ['.', 'O', 'O', '.', '.', '.'],
 ['O', 'O', 'O', 'O', '.', '.'],
 ['O', 'O', 'O', 'O', 'O', '.'],
 ['.', 'O', 'O', 'O', 'O', 'O'],
 ['O', 'O', 'O', 'O', 'O', '.'],
 ['O', 'O', 'O', 'O', '.', '.'],
 ['.', 'O', 'O', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.']]

height = 9
width = 6
new_grid = []
for i in range(width):
    row = []
    for j in range(height):
        row.append(grid[j][i])
    new_grid.append(row)


for i in range(width):
    for j in range(height):
        print(new_grid[i][j], end='')
    print()
