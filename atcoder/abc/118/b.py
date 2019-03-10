def main():
  N, M = map(int, input().split())
  anss = []
  for _ in range(N):
    anss.append(set(list(map(int, input().split()))[1:]))

  # print(ans)
  result = set([i for i in range(31)])
  for ans in anss:
    result = result & ans

  print(len(result))
  

main()