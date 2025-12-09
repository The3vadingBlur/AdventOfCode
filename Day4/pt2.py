from pathlib import Path
import math

with open("input.txt") as f:
    grid = f.read().splitlines()
grid = [list(row) for row in grid]

rows = len(grid)
cols = len(grid[0])

reachable_rolls = 0
removed_rolls = 0

offsets = [ 
    (-1,-1), (-1,0), (-1,1),
    (0,-1),          (0,1),
    (1,-1),  (1,0),  (1,1)
]

def reachable_rolls_function():
    global reachable_rolls
    global removed_rolls
    temp_reached_rolls = 0
    temp_removed_rolls = 0
    accessible_rolls = [] 
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                count = 0 
                for dr, dc in offsets:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == '@':
                            count +=1 
                if count < 4:
                    temp_reached_rolls += 1
                    accessible_rolls.append((r,c))
                    temp_removed_rolls += 1
    if temp_reached_rolls > 0 and temp_removed_rolls > 0:
        for r,c in accessible_rolls:
            grid[r][c] = '.'
            print ("rolls were removed")
            removed_rolls += 1
            reachable_rolls += 1
        return True
    else:
        return False

def main(): 
    while reachable_rolls_function():
        print(removed_rolls)


main() 



