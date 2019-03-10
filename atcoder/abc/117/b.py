def main():
  # N_max < sum(not N_max)
  N = int(input())
  Ls = map(int, input().split())

  Ls = sorted(Ls, reverse=True)
  N_max = Ls[0]
  N_sum = sum(Ls[1:])
  if N_max < N_sum:
    print('Yes')
  else:
    print('No')



main()