# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_D&lang=jp

def main():
    # n = int(input())
    # N = [int(input()) for _ in range(n)]
    
    # Case 1
    n = 6
    N = [5,3,1,3,4,3]
    # # Case 2
    # n = 3
    # N = [4,3,2]


    # O(n)
    minv = N[0]
    maxv = -10000000000000000
    for i in range(1, len(N)):
        maxv = max(maxv, N[i] - minv)
        minv = min(minv, N[i])
    print(maxv)

    # O(n^2)
    # N = N[::-1]
    # result = -100000000000
    # for i in range(len(N)):
    #     for j in range(i+1, len(N)):
    #         tmp = N[i] - N[j]
    #         if tmp >= result:
    #             # print(N[i], N[j])
    #             result = tmp
    # print(result)



main()