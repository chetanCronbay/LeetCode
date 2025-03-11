from typing import List

def findMaxFish(grid: List[List[int]]) -> int:
    def search(grid, row, col, visited):
        # Boundary conditions and base cases
        if (
            row < 0 or row >= len(grid) or
            col < 0 or col >= len(grid[0]) or
            (row, col) in visited or
            grid[row][col] == 0
        ):
            return 0

        # Mark current cell as visited
        visited.add((row, col))

        # Start fish count with the current cell
        fishcount = grid[row][col]

        # Explore all four neighbors (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            fishcount += search(grid, row + dr, col + dc, visited)

        return fishcount

    maxval = 0
    visited = set()  # Use a set to track visited cells

    # Iterate through all cells in the grid
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] > 0 and (row, col) not in visited:
                # Start a new DFS if the cell has fish and is unvisited
                maxval = max(maxval, search(grid, row, col, visited))

    return maxval

# Example grid
grid = [[0, 2, 1, 0], 
        [4, 0, 0, 3], 
        [1, 0, 0, 4], 
        [0, 3, 2, 0]]

print(findMaxFish(grid))
