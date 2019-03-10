def main():
  H, W = map(int, input().split(' '))
  h, w = map(int, input().split(' '))
  
  a = H*W
  b = (h * W) + (w * H) - h * w
  print(a - b)
  


main()