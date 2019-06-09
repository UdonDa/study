# 二分探索
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_B&lang=jp

n = int(input())
s = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

s = sorted(s)

def binary_search(A, key):
    left = 0
    right = len(A)
    while left < right:
        mid = (left + right) // 2
        if A[mid] == key:
            return mid
        elif key < A[mid]:
            right = mid
        elif key > A[mid]:
            left = mid


keys = [binary_search(s, t) for t in T]
print(len(keys))