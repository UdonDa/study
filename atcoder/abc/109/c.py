from functools import reduce

def gcds(a, b):
	while b:
		a, b = b, a % b
	return a

def gcd(*num):
    return reduce(gcds, *num)

def main():
    N, X = map(int, input().split(' '))
    x_n = list(map(int, input().split(' ')))

    x_n = sorted(x_n)
    x_n = [n - X for n in x_n] # スタートを0からに
    
    print(abs(gcd(x_n)))
    return

main()