def main():
  S = list(input())
  T = input()

  t = ''.join(S)
  if t == T:
    print('Yes')
    return

  for _ in range(len(S)-1):
    last = S[-1]
    S.pop(-1)
    S.insert(0, last)
    t = ''.join(S)
    # print(t, T, t == T)

    if t == T:
      print('Yes')
      return
      
  print('No')
  return

main()