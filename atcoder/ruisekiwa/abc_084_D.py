from itertools import accumulate

def eratosunetesu_no_furui(n):
  # エラトステネスのふるい
  # 素数
  # n >= 2:
  data = [i for i in range(2, n+1)]
  for d in data:
    data = [x for x in data if (x == d or x % d != 0)]
  return data

max = 10


Q = int(input())
L = [0] * Q
R = [0] * Q

for i in range(Q):
  L[i], R[i] = list(map(int, input().split()))

max_R = max(R)
