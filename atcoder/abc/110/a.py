_in = list(map(int, input().split(' ')))
_in = sorted(_in)
a = int('{}{}'.format(_in[-1], _in[-2]))
print('{}'.format(_in[0] + a))

