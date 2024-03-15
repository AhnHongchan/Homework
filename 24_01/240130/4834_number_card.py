T = int(input())
for i in range(1, T+1):
    num = int(input())
    case = list(map(int, input()))
    k = 100
    cnt = [0] * (k+1)
    for j in range(0, len(case)):
        cnt[case[j]] += 1
        max_num = cnt[0]
        for m in range(k+1):
            if cnt[m] >= max_num:
                max_num = cnt[m]
                r = m

    print(f'#{i} {r} {max_num}')    




