import numpy as np
from scipy import ndimage

with open('day-four.txt') as f:
    grid = f.read().splitlines()

grid = [list(line) for line in grid]

for line in grid:
    for i in range(len(line)):
        if line[i] == '@':
            line[i] = 1
        else:
            line[i] = 0

grid = np.array(grid)

kernel = np.array([[1, 1, 1],
                      [1, 0, 1],
                      [1, 1, 1]])

nbhr_counts = ndimage.convolve(grid, kernel, mode='constant', cval = 0)

print(np.sum((grid == 1) & (nbhr_counts < 4)))
