from math import prod
from itertools import combinations

arr = []        # Array for numbers
n = 2           # How many elements to sum
target = 2020   # Target sum

# Open the file of numbers to check
with open('input.txt', 'r', encoding='utf-8') as f:
  arr = list(map(int, f.readlines()))
  
f.close()


def find_pairs(arr, n, target):
    return [pair for pair in combinations(arr, n) if sum(pair) == target]


print(prod(find_pairs(arr, n, target)[0]))
