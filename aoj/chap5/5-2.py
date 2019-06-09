# 線形探索
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_A&lang=jp

n = int(input())
s = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

print(len(set(s) & set(T)))