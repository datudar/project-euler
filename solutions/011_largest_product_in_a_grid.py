# Source
# ======
# https://www.hackerrank.com/contests/projecteuler/challenges/euler011
#
# Problem
# =======
# In the 20x20 grid (see Source for grid), four numbers along a diagonal 
# line have been marked in bold.
#
# The product of these numbers is 26 x 63 x 78 x 14 = 1788696.
#
# What is the greatest product of four adjacent numbers in the same direction 
# (up, down, left, right, or diagonally) in the 20x20 grid?
#
# Input Format
# ============
# Input consists of 20 lines each containing 20 integers.
#
# Constraints
# ============
# 0 <= Each integer in the grid <= 100
#
# Output Format
# =============
# Print the required answer.

grid_size = 20

grid = []
for grid_i in range(grid_size):
   grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
   grid.append(grid_t)
   
# Note: For this grid, we will assume that (0,0) is the location of the 
# top-left corner and (grid_size, grid_size) is the bottom-right corner
product = []
for y in range(grid_size):
    for x in range(grid_size):
        # left-right
        if x+3 < grid_size:
             product.append(grid[y][x] * grid[y][x+1] * grid[y][x+2] * grid[y][x+3])
        # up-down
        if y+3 < grid_size:
             product.append(grid[y][x] * grid[y+1][x] * grid[y+2][x] * grid[y+3][x])
        # back-diagonal
        if x+3 < grid_size and y+3 < grid_size:
             product.append(grid[y][x] * grid[y+1][x+1] * grid[y+2][x+2] * grid[y+3][x+3])  
        # forward-diagonal
        if x >= 3 and y+3 < grid_size:
             product.append(grid[y][x] * grid[y+1][x-1] * grid[y+2][x-2] * grid[y+3][x-3])    
            
print(max(product))