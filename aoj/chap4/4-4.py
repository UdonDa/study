# 連結リスト
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_C&lang=jp

from collections import deque

def main():
    n = int(input())
    d = deque()
    for _ in range(n):
        command = input()
        if command == "deleteFirst":
            d.popleft()
        elif command == "deleteLast":
            d.pop()
        else:
            com, num = command.split(" ")
            if com == "insert":
                d.appendleft(num)
            elif com == "delete":
                try:
                    d.remove(num)
                except:
                    pass
    print(" ".join(d))


main()