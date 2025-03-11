row = {}
col = {}
count = 0
grid = [[1,1,0,0],[0,1,1,0],[0,0,1,0],[0,0,0,1]]
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 1:
            if r not in row:
                row[r] = 0
            if c not in col:
                col[c] = 0
            row[r] += 1
            col[c] += 1
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 1:
            if row[r] > 1 or col[c] > 1:
                count += 1

print(count)