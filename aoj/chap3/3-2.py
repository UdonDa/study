# 挿入ソート
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_A

def show(array):
    for i in range(len(array)):
        if (i+1) >= len(array):
            print(array[i])
        else:
            print(array[i], end=' ')

def main():
    N = int(input())
    A = list(map(int, input().split(' ')))

    # N = 10
    # A = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    show(A)
    # O(N^2) 整列されてないとかなり時間がかかる.
    for i in range(1, N):
        v = A[i] # i番目の値
        j = i - 1 # i-1番目
        while (j >= 0) and (A[j] > v):
            A[j+1] = A[j]
            j -= 1
        A[j+1] = v
        show(A)

main()