# https://atcoder.jp/contests/abc103


A = map(int, input().split(' '))
A = sorted(A)

result = 0
for i in range(len(A)-1):
  result += A[i+1] - A[i]
print(result)