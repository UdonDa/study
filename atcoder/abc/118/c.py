from fractions import gcd
import numpy as np

N = int(input())
A = np.array([int(i) for i in input().split()])

a = A[0]
for b in A[1:]:
  a = gcd(a, b)

print(a)


# def is_include_0(x):
#   if 0 in x:
#     x.remove(0)

#   if 0 in x:
#     return is_include_0(x)
#   else:
#     return x
  

# def main():
#   N = int(input())
#   monsters = list(map(int, input().split()))

#   monsters = sorted(monsters)
#   # print(monsters)
#   prev = None
#   while True:
#     # print('==============================')
#     monsters = sorted(monsters)
#     prev = monsters
#     # print(monsters)
    
#     for i in range(1, len(monsters)):
#       monsters[i] = monsters[i] % monsters[0]

#     # print(monsters)
#     if 0 in monsters:
#       monsters = list(set(monsters))
#       monsters.remove(0)
#       monsters = sorted(monsters)

#     # print(monsters)
#     if len(monsters) == 2:
#       if monsters[1] < monsters[0]:
#         monsters[0] -= monsters[1]
#         continue
#       # print('a')
#       last = monsters[1] - monsters[0]
#       if last == 0:
#         break
#       monsters[0] = last
#       monsters.remove(monsters[1])
#       # print(monsters)

#     if len(monsters) == 1:
#       break

#     if prev == monsters:
#       monsters[0] -= monsters[1]



#   print(monsters[0])

# main()




# 4
# 2 10 8 40