from collections import Counter


def main():
    n = int(input())
    v_n = input().split(' ')
    
    gu = Counter(v_n[::2])
    ki = Counter(v_n[1::2])

    guusuu = gu.most_common()
    kisuu = ki.most_common()

    if guusuu[0][0]==kisuu[0][0]:
        if len(guusuu)==1 and len(kisuu)==1:
            print(guusuu[0][1]) # n=4, `4 4 4 4`
        else:
            print(min(n - guusuu[0][1] - kisuu[1][1], n - guusuu[1][1] - kisuu[0][1]))
    else:
        print(n - guusuu[0][1] - kisuu[0][1])

main()
#     # print(guusuu)
#     # print(kisuu)

#     # print(len(guusuu), len(kisuu))
#     # if len(set(guusuu)) == 1:
#     #     # 偶数番目１種類
#     #     print(n//2 - kisuu[0][1])
#     # elif len(set(kisuu)) == 1:
#     #     # 奇数番目１種類
#     #     print(n//2 - guusuu[0][1])
#     # # ２種類以上
#     # elif guusuu[0][0] == kisuu[0][0]:
#     #     # 最頻値が同じ時，どちらかは譲らないといけない
#     #     #   => ２番目の最頻値で書き換えるべき
#     #     result = min(n - guusuu[0][1] - kisuu[1][1], n- guusuu[1][1] - kisuu[0][1])
#     #     print(result)
#     # else:
#     #     # 最頻値が違う時，どちらも最頻値で書き換え
#     #     print(n - guusuu[0][1] - kisuu[0][1])


# main()