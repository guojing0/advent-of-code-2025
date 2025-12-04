import numpy as np
from scipy.ndimage import convolve

with open('day-four.txt') as f:
    lines = f.read().splitlines()

# Parse grid: @ = 1, . = 0
grid = np.array([[1 if c == '@' else 0 for c in line] for line in lines])

# Kernel to count 8 adjacent neighbors
kernel = np.array([[1, 1, 1],
                   [1, 0, 1],
                   [1, 1, 1]])

nbhr_counts = convolve(grid, kernel, mode='constant', cval=0)

# Count @ cells with fewer than 4 @ neighbors
print(np.sum((grid == 1) & (nbhr_counts < 4)))
