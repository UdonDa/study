ONE = 2
TWO = 5
THREE = 5
FOUR = 4
FIVE = 5
SIX = 6
SEVEN = 3
EIGHT = 7
NINE = 6


def main():
    N, M = map(int, input().split(' '))
    dic = {} # 使える数字
    Am = list(map(int, input().split(' ')))
    for a in Am:
        dic[str(a)] = a
    print(Am, dic)

    dic2 = {}
    for a in dic.values():
        print(type(a))
        if a == 1:
            dic2[str(a)] = ONE
        elif a == 2:
            dic2[str(a)] = TWO
        elif a == 3:
            dic2[str(a)] = THREE
        elif a == 4:
            dic2[str(a)] = FOUR
        elif a == 5:
            dic2[str(a)] = FIVE
        elif a == 6:
            dic2[str(a)] = SIX
        elif a == 7:
            dic2[str(a)] = SEVEN
        elif a == 8:
            dic2[str(a)] = EIGHT
        elif a == 9:
            dic2[str(a)] = NINE
    print(dic2)
    dic3 = {}
    for k, v in sorted(dic2.items(), key=lambda x: x[1]):
        dic3[k] = v
    print(dic3)
    keys = list(dic3.keys())
    print(keys)
    
    result = ''
    i = 0
    while True: 
        if N - dic3[keys[i]] >= 0:
            print(dic3[keys[i]])
            N -= dic3[keys[i]]
            result += keys[i]
            print(result)
        else:
            i += 1
        

        if N == 0:
            break
        
    # print(result)

main()  