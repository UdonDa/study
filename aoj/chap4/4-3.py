# キュー
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_B&lang=jp

def main():
    n, q = map(int, input().split(" "))
    schedules = [input().split(" ") for _ in range(n)]
        
    # print(schedules)

    isFinished = True
    total = 0
    # print("--- Start ---")
    while isFinished:
        if len(schedules) == 0:
            isFinished = False
            break

        name, time = schedules.pop(0)
        time = int(time)
        if time > q:
            time -= q
            total += q
            schedules.append([name, time])
        else:
            total += time
            print(f"{name} {total}")

main()