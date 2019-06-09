# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_D&lang=jp
# 面積計算

from collections import deque

def main():
    a = input()
    d = deque()

    stack_1 = deque()
    stack_2 = deque()
    for i, c in enumerate(a):
        if c == "\\":
            stack_1.append(i)
        elif c == "/":
            a = 0
            if len(stack_1) > 0:
                while True:
                    if len(stack_2) > 0 and stack_2[-1][0] > stack_1[-1]:
                        a += stack_2[-1][1]
                        stack_2.pop()
                    else:
                        break
            a += i - stack_1[-1]
            stack_2.append([stack_1[-1], a])
            stack_1.pop()
    for i in range(len(p)):
        stack_2[i] = stack_2[i][1]
    if len(stack_2) > 0:
        print(sum(stack_2))
        print(len(stack_2), end = " ")
        print(" ".join(map(str, stack_2)))
    else:
        print(0)
        print(0)


main()