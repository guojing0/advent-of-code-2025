import operator
from functools import reduce

import numpy as np

with open('day-six.txt') as f:
    lines = [line.split() for line in f]

ops = {'*': operator.mul, '+': operator.add}
matrix = np.array([[int(x) for x in row] for row in lines[:-1]]).T
results = [reduce(ops[op], row) for row, op in zip(matrix, lines[-1])]

print(sum(results))
