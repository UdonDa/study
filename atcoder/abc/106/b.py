def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

def main():
    N = int(input())
    result = 0
    for n in range(1, N+1, 2):
        div = get_divisors(n)
        if len(div) == 8:
            result += 1

    print(result)


main()