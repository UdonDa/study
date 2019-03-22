n = list(input())

result = ""

for a in n:
  if a == '1':
    result += '9'
  else:
    result += '1'


print(result)