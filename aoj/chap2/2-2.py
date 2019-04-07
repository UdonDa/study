def main():
    n = [25, 36, 4, 55, 71, 18, 0, 71, 89, 65]
    # s = list(map(int, input().split(' ')))
    print(sorted(n, reverse=True)[0:3])

def algorithm3():
    N = [25, 36, 4, 55, 71, 18, 0, 71, 89, 65]
    scores = [0]*100
    
    for n in N:
        scores[n] += 1
    
    count = 0
    results = []
    for i, score in enumerate(scores[::-1]):
        if score >= 1:
            for _ in range(score):
                results.append(100 - (i+1))
                count += 1
        if count >= 3:
            print(results)
            return
        
        

    


# main()
algorithm3()