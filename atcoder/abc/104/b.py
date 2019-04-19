def main():
  s = list(input())
  if s[0] != 'A':
    print('WA')
    return

  C_counter = 0
  for n in s[2:-1]:    
    if n == 'C':
      C_counter += 1

  if C_counter != 1:
    print('WA')
    return

  for n in s:
    if n == 'A' or n == 'C':
      continue
    if not n.islower():
      print('WA')
      return
  print('AC')
  return




main()