def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def main():
    N = int(input())
    An = list(map(int, input().split(' ')))


    An = sorted(An)
    An = [gcd(a_n, An[0]) for a_n in An]
    print(min(An))

main()