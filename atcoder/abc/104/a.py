# https://atcoder.jp/contests/abc104?lang=ja

def main():
  R = int(input())

  if R < 1200:
    print('ABC')
  elif R < 2800:
    print('ARC')
  else:
    print('AGC')
main()