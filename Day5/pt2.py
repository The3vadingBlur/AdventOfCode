from pathlib import Path
import math

with open("input.txt") as f:
    lines = f.read().splitlines() 

ranges = []
ids = [] 


# I know I dont need all this, but the code is here and I might as well reuse it. I'm lazy. 
for line in lines:
    if line.strip() == '':
        continue 
    if '-' in line.strip():
        start,end = map(int, line.strip().split('-'))
        ranges.append((start,end))
    else:
        ids.append(int(line.strip()))
    # print("\n ranges are ", ranges, " and ids are ", ids)

# part 2 babbyyyy lets go 

merged_ranges = []
total_ids = 0 
ranges.sort()
current_start, current_end = ranges[0]
for start, end in ranges[1:]:
    if start <= current_end + 1:
        current_end = max(end, current_end)
    else: 
        merged_ranges.append((current_start, current_end))
        current_start,current_end = start, end
merged_ranges.append((current_start,current_end))

for start,end in merged_ranges:
    total_ids += end-start+1

print(total_ids)
