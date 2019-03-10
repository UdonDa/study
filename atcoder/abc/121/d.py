import numpy as np


A, B = map(int, input().split(' '))
values = np.array([A-1, B])
print(np.bitwise_xor(A-1, B))

# result = values[0]
# for value in values[1:]:
#   result = np.bitwise_xor(result, value)
# print(int(result))

# print(f(B) ^ f(A-1))