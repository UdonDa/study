def main():

  N, M = map(int, input().split(' '))

  pairs = []
  for _ in range(N):
    a, b = map(int, input().split(' '))
    pairs.append([a, b])
  # print(pairs)

  pairs = sorted(pairs, key = lambda x: x[0])
  # print(pairs)

  yen = 0
  count = 0
  # for m in range(M):
  for a, b in pairs:
    if count >= M:
      # print("over - 1")
      break

    for mo in range(b):
      count += 1
      yen += a
      # print(mo, a, yen, count)
      if count >= M:
        # print("over - 2")
        break
  print(yen)

main()