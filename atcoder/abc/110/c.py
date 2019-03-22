def solve(S, T):
    StoT = {}
    TtoS = {}
    for s, t in zip(S, T):
        if s not in StoT:
            StoT[s] = t
        if t not in TtoS:
            TtoS[t] = s
        
        if StoT[s] != t or TtoS[t] != s:
            # 別の文字に写像してしまってる.
            return False

    return True
        


S = list(input())
T = list(input())

bool = solve(S, T)
if bool:
    print('Yes')
else:
    print('No')

# abcdefghijklmnopqrstuvwxyz
# ibyhqfrekavclxjstdwgpzmonu