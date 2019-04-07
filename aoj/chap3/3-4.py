# 選択ソート: 各計算ステップでの1つの最小値を選択していくアルゴリズム
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_2_B&lang=jp
# 離れた要素を交換するので，安定ではない（左右の順番が入れ替わる
# O(N^2)

def show(array):
    for i in range(len(array)):
        if (i+1) >= len(array):
            print(array[i])
        else:
            print(array[i], end=' ')

def main():
    N = int(input())
    A = list(map(int, input().split(' ')))

    # N = 6
    # A = [5,6,4,2,1,3]
    changed_num = 0

    for i in range(0, N):
        minj = i
        for j in range(i, N):
            if A[minj] > A[j]: # i番目以上の最小を求める
                minj = j
        if A[i] != A[minj]:
            A[i], A[minj] = A[minj], A[i]
            changed_num += 1

    show(A)
    print(changed_num)


main()