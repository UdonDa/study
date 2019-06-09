# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_A&lang=jp
# スタック, 逆ポーランド記法

def main():
  inps = list(input().split(" "))
  # print(inps)

  stack = []
  for inp in inps:
    a = int(stack.pop(-2))
    b = int(stack.pop(-1))
    if inp == "+":
      stack.append(a+b)
    elif inp == "-":
      stack.append(a-b)
    elif inp == "*":
      stack.append(a*b)
    else:
      stack.append(inp)
    # print(inp, type(inp), stack)
  print(int(stack[0]))

main()