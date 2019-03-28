def main():
    A, B = map(int, input().split(' '))
    for c in range(1, 4):
        re = A * B * c
        if re % 2 == 1:
            print('Yes')
            return
    print('No')
    return

main()