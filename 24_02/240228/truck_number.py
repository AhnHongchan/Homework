T = int(input())
for tc in range(1, T+1):
    N = int(input())
    time = []
    for _ in range(N):
        start, end = map(int, input().split())
        time.append((start, end))
    
    time.sort(key = lambda x: x[1])

    schedule = [time[0]]
    for i in range(1, N):
        if time[i][0] < schedule[-1][1]:
            pass
        else:
            schedule.append(time[i])
    print(f'#{tc} {len(schedule)}')
            