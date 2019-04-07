def main():
  a = int(input())
  b = int(input())
  c = int(input())
  d = int(input())
  e = int(input())
  k = int(input())

  counter = False
  antena = [a,b,c,d,e]
  for i in range(len(antena)-1):
    p = antena[i]
    for j in range(i, len(antena)):
      q = antena[j]
      if (q-p) > k:
        counter = True
    
  if counter:
    print(':(')
    
  else:
    print('Yay!')
    

main()