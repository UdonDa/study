def main():
  city = {}
  states = {1:0, 2:0, 3:0, 4:0, 5:0}
  N = int(input())
  for i in range(5):
    city[str(i+1)] = int(input())
  
  print('--------------')
  print(N, city, states)

  isFinish = False
  minute = 0
  while isFinish:
    


    if states[5] == N:
      isFinish = True

main()