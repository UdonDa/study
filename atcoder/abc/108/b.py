def main():
    N, M = map(int, input().split(' '))
    Ks = [list(map(int, input().split(' ')))[1:] for _ in range(N)]
    
    duplicated = set(Ks[0])
    for i in range(1, len(Ks)):
        a = set(Ks[i])
        duplicated = duplicated & a

    print(len(duplicated))


    
main()