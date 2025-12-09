from pathlib import Path
import math

with open("input.txt") as f:
    grid = f.read().splitlines()

rows = len(grid)
cols = len(grid[0])

reachable_rolls = 0
removed_rolls = 0 

offsets = [ 
    (-1,-1), (-1,0), (-1,1),
    (0,-1),          (0,1),
    (1,-1),  (1,0),  (1,1)
]

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == '@':
            count = 0 
            for dr, dc, in offsets:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == '@':
                        count +=1 
            if count < 4:
                reachable_rolls += 1 

print(reachable_rolls)


