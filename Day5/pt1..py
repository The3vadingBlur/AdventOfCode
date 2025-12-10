from pathlib import Path
import math

with open("input.txt") as f:
    lines = f.read().splitlines() 

ranges = []
ids = [] 
fresh = 0 

for line in lines:
    if line.strip() == '':
        continue 
    if '-' in line.strip():
        start,end = map(int, line.strip().split('-'))
        ranges.append((start,end))
    else:
        ids.append(int(line.strip()))
    # print("\n ranges are ", ranges, " and ids are ", ids)

for id in ids:
    for id_range in ranges:
        start, end = id_range
        if start <= id <= end:
            fresh += 1 
            break

print(fresh)

