def main():
    N = int(input())

    for i in range(N):
        for j in range(N):
            n = 4*i + 7*j
            if n == N:
                print('Yes')
                return
    print('No')
    return

main()