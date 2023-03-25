set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# union of two sets
union = set1.union(set2)
print(union)  # output: {1, 2, 3, 4, 5, 6, 7, 8}

# intersection of two sets
intersection = set1.intersection(set2)
print(intersection)  # output: {4, 5}

# difference of two sets
difference = set1.difference(set2)
print(difference)  # output: {1, 2, 3}
