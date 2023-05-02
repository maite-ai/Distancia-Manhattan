def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a, b))

A = [3, 5, 7, 9]
B = [5, 4, 7, 6]


print(manhattan(A, B))