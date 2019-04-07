def main():
  inp = []
  for i in range(5):
    x = int(input())
    if x % 10 == 0:
      inp.append([x, 0])
    else:
      inp.append([x, 10 - (x % 10)])
  inp = sorted(inp, key=lambda x: x[1]) 
  # print(inp)

  result = 0
  for i, n in enumerate(inp):
    # print(i, n[0], n[1], result)
    if (i+1) == len(inp):
      result += n[0]
      continue
    
    result += n[0] + n[1]

  print(result)
    
    
    
    
main()

# def main():
#   A = int(input())
#   B = int(input())
#   C = int(input())
#   D = int(input())
#   E = int(input())

#   orders = sorted([A,B,C,D,E])
#   lunch = {}
#   # wattayatu = [10 - (n % 10) for n in orders if n % 10 != 0]
#   n10 = []
#   for i, n in enumerate(orders):
#     if n % 10 == 0:
#       n10.append(n)
#     else:
#       lunch['{}-{}'.format(n, i)] = 10 - (n % 10)
#   # print('lunch: ', lunch)
#   lunch2 = {}
#   for i, (k, v) in enumerate(sorted(lunch.items(), key=lambda x: x[1])):
#     k = k.split('-')[0]
#     # print(k, i)
#     lunch2['{}-{}'.format(k, i)] = v

#   # print('n10: ', n10)
#   # print('lunch2: ', lunch2)
#   result = sum(n10)
#   for i, (k, v) in enumerate(lunch2.items()):
#     k = int(k.split('-')[0])
#     if (i+1) == len(lunch2):
#       result += k
#     else:
#       result += k + v
#   print(result)


# main()