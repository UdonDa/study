# ハッシュ
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_C&lang=jp


n = int(input())
a = [list(input().split()) for _ in range(n)]

strs = set()

for c, s in a:
    if c == "insert":
        strs.add(s)
    elif c == "find":
        if s in strs:
            print("yes")
        else:
            print("no")