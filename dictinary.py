from functools import reduce

numLists = [[0, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
new = reduce(lambda x, y: x + y, numLists, [2])


print(list(reduce(lambda x, y: x  y, new)))