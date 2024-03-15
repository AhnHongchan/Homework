T = int(input())
for i in range(1, T+1):
    num = input()
    cnt = [0] * 10
    tri = 0
    straight = 0
    for j in num:
        cnt[int(j)] += 1

    k = 0
    while k < 10:
        if cnt[k] >= 3:
            cnt[k] -= 3
            tri += 1
            continue
        k += 1

    k = 0
    while k < 8:    
        if cnt[k] >= 1 and cnt[k + 1] >= 1 and cnt[k + 2] >= 1:
            cnt[k] -= 1
            cnt[k + 1] -= 1
            cnt[k + 2] -= 1
            straight += 1
            continue
        else:
            k += 1

    if tri + straight == 2:
        print(f'#{i} Baby Gin')
    else:
        print(f'#{i} Lose')
