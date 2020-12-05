import numpy as np
import math

# Array of tuples to represent the slope(s)
slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
#slopes = [(3,1)]

lines = []
with open('C:/Users/durha/Desktop/trees.txt', 'r', encoding='utf-8') as f:
    trees = f.read().splitlines()

f.close()

def count_trees(trees, slopes, op = 'sum'):
    treeCountArray = []
    for right, down in slopes:
        # Remove the initial line(s) of trees for downward slope
        treeCheck = trees[down:]
        count = 0
        i = right
        for index, tree in enumerate(treeCheck):
            # Skip lines depending on {down}
            if down != 1 and index % down != 0:
                continue
            # Correct for iterator out of bounds
            if i >= len(tree):
                i -= len(tree)
            # Count the trees
            if tree[i] == '#':
                count += 1
            # Increment the iterator
            i += right
        # Return the count of trees
        treeCountArray.append(count)
    
    if op == 'sum':
        return np.sum(treeCountArray)
    elif op == 'prod':
        return math.prod(treeCountArray)
    # return treeCountArray if op is not sum or prod
    return treeCountArray



# print(count_trees(trees, slopes, 'sum'))

print(count_trees(trees, slopes, 'prod'))
