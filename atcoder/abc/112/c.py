from math import fabs

def main():
  N = int(input())

  cors = [list(map(int, input().split())) for _ in range(N)]
  cors_sorted = sorted(cors, key = lambda x: x[2], reverse=True)
  top_x, top_y, top_h = cors_sorted[0]

  for C_x in range(101):
    for C_y in range(101):
      H = top_h + fabs(top_x - C_x) + fabs(top_y - C_y)
      if all([h == max(H - fabs(x - C_x) - fabs(y - C_y), 0) for x,y,h in cors_sorted]):
        print(C_x, C_y, int(H))
        return


main()