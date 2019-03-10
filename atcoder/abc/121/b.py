def main():

  N, M, C = map(int, input().split(' '))
  Bs = input().split(' ')
  As = []
  for _ in range(N):
    As.append(input().split(' '))

  # print('----------')
  # print(N, M, C)
  # print(Bs)
  # print(As)

  result = 0
  for A in As:
    tmp = 0
    for a, b in zip(A, Bs):
      tmp = tmp + int(a) * int(b)
    tmp += int(C)

    if tmp > 0:
      result += 1

  print(result)


main()