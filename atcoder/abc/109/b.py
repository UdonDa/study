def main():
    N = int(input())
    W = [input() for _ in range(N)]
     
    # まだ発話していない
    w = set(W)
    if len(W) != len(w):
        print('No')
        return

    # 先頭は直前の単語の末尾と一致
    for i in range(len(W)-1):
        be = W[i][-1]
        af = W[i+1][0]
        if be != af:
            print('No')
            return
    print('Yes')
    return



main()