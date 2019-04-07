# バブルソート
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_2_A&lang=jp

def show(array):
    for i in range(len(array)):
        if (i+1) >= len(array):
            print(array[i])
        else:
            print(array[i], end=' ')

def main():
    N = int(input())
    A = list(map(int, input().split(' ')))

    # N = 5
    # A = [5,3,2,4,1]

    change_num = 0

    # O(N^2) 
    isFisnished = True
    while isFisnished:
        isFisnished = False
        for i in range(N-1, 0, -1):
            if A[i-1] > A[i]: # A[i-1] >= A[i] とすると，値が等しい隣同士でも交換をするので，安定じゃなくなる.
                A[i-1], A[i] = A[i], A[i-1]
                change_num += 1
                isFisnished = True

    show(A)
    print(change_num) # 交換回数は列の乱れ度を表す.



    


main()