from itertools import accumulate

# 区間[N-k, N) の総和の最大値

while True:
  n, k = map(int, input().split())
  if n == 0:
    break
  a_n = [int(input()) for _ in range(n)]
  _ = input()

  a_n = list(accumulate(a_n))
  # print(a_n)

  result = -99999999999999

  for i in range(n-k):
    val = a_n[k+i] - a_n[i]
    if result < val:
      result = val


  print(result)