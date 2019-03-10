def main():
  n, T = map(int, input().split())
  kiro = []
  for _ in range(n):
    c_i, t_i = map(int, input().split())
    kiro.append([c_i, t_i])

  
  
  kiro = sorted(kiro, key=lambda x: x[0])

  for c, t in kiro:
    if t <= T:
      print(c)
      return
  print('TLE')

main()