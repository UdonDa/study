def main():
    N = int(input())

    result = 0
    if 0 <= N <= 111:
        result = 111
    elif 111 < N <= 222:
        result = 222
    elif 222 < N <= 333:
        result = 333
    elif 333 < N <= 444:
        result = 444
    elif 444 < N <= 555:
        result = 555
    elif 555 < N <= 666:
        result = 666
    elif 666 < N <= 777:
        result = 777
    elif 777 < N <= 888:
        result = 888
    elif 888 < N <= 999:
        result = 999

    print(result)
    

main()