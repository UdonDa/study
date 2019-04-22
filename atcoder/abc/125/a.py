def main():
    a, b, c = map(int, input().split(' '))
    if b > c > a:
        print('Yes')
    elif a > c > b:
        print('Yes')
    else:
        print("No")

main()