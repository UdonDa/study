from collections import Counter

def main():
    N = int(input())
    S = input()

    res = dot = S.count(".")
    sha = 0
    for i in range(N):
        if S[i] == "#":
            sha += 1
        else:
            dot -= 1
        tmp = sha + dot
        res = min(tmp, res)
    print(res)


def main2():
    from itertools import accumulate
    # 累積和
    N = int(input())
    S = input()

    kuro = [0] * N
    shiro = [0] * N

    for i, s in enumerate(S):
        if s == "#":
            kuro[i] = 1
        else:
            shiro[i] = 1
    
    print(kuro, shiro)
    # 累積和
    kuro = [0] + kuro
    kuro = list(accumulate(kuro))
    shiro = [0] + shiro[::-1]
    shiro = list(accumulate(shiro))[::-1]
    print(kuro, shiro)

    ans = []
    for i in range(N+1):
        ans.append(kuro[i] + shiro[i])
    print(ans)
    print(min(ans))

    


main2()
# def main():
#     _ = int(input()) ###
#     S = list(input())

#     # C = Counter(S)

#     result = 10000
#     for i in range(1, len(S)+1):
#         left, right = Counter(S[:i]), Counter(S[i:])
#         count_sharp = left['#']
#         count_dot = right['.']

#         total = count_sharp + count_dot
#         # print(left, right, count_sharp,count_dot, total)
#         result = min(result, total)
#     print(result)


    
    # count_sharp = S.count('#')
    # count_dot = S.count('.')
    # print(count_sharp, count_dot, count_sharp > count_dot) ###
    # count = 0

    # for i in range(1, len(S)):
        
    #     print(S, end=' ') ###
    #     one = S[i-1]
    #     two = S[i]
        
    #     if count_sharp > count_dot: # . -> #
    #         if (one == '#') and (two == '.'):
    #             count += 1
    #             S[i] = '#'
    #         # elif (one == '#') and (two == '#') :
    #         #     S[i] = '.'
    #         #     count += 1
    #     else:
    #         if (one == '#') and (two == '.'):
    #             if i < len(S) - 1:
    #                 # if '.' not in S[i+1:]:
    #                 print('ss')
    #                 count += 1
    #                 S[i] = '.'
    #         elif (one == '.') and (two == '#'):
    #             if i < len(S) - 1:
    #                 if S[i+1] == '#':
    #                     if '.' in S[i+1:]:
    #                         print('unko', i, S[i], end=' ')
    #                         count += 1
    #                         S[i] = '.'
    #                 elif S[i+1] == '.':
    #                     count += 1
    #                     S[i] = '.'
    #         elif (one == '#') and (two == '#'):
    #             S[i] = '.'
    #             count += 1
    #     print(count, end=' ') ###
    #     print(S) ###

    # print(count)
    # #..#.#....##...# -> (.)..(.).(.)....(.)(.)...#

    # ###..#.##

    # # ...##...#..###

# main()