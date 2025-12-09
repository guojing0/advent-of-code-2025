with open('day-seven.txt') as f:
    lines = f.read().splitlines()

# Find starting column (where S is)
start_col = lines[0].index('S')
num_cols = len(lines[0])

# Part 1: Count the number of splits
# Track which columns have beams (binary: has beam or not)
beams = [False] * num_cols
beams[start_col] = True
split_count = 0

for i in range(len(lines) - 1):
    new_beams = [False] * num_cols
    
    for j in range(num_cols):
        if beams[j]:
            if lines[i + 1][j] == '^':  # Splitter
                if j > 0:
                    new_beams[j - 1] = True
                if j < num_cols - 1:
                    new_beams[j + 1] = True
                split_count += 1
            else:  # Empty space
                new_beams[j] = True
    
    beams = new_beams

print(f"Part 1: {split_count}")

# Part 2: Track number of timelines at each column
# Instead of binary (beam exists or not), we track counts
path_counts = [0] * num_cols
path_counts[start_col] = 1  # Start with 1 timeline at S

# Process each row transition
for i in range(len(lines) - 1):
    new_counts = [0] * num_cols
    
    for j in range(num_cols):
        if path_counts[j] > 0:
            # Check what's in the next row at this column
            if lines[i + 1][j] == '^':  # Splitter
                # Each timeline splits into 2: one goes left, one goes right
                if j > 0:
                    new_counts[j - 1] += path_counts[j]
                if j < num_cols - 1:
                    new_counts[j + 1] += path_counts[j]
            else:  # Empty space
                # Timelines continue straight down
                new_counts[j] += path_counts[j]
    
    path_counts = new_counts

# Total timelines = sum of all paths that reached the bottom
print(f"Part 2: {sum(path_counts)}")

