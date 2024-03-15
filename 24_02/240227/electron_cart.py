def bat(x):
    if x == N:
        result.append(path[:])
        return
    
    for i in range(1, N):
        if used[i] == True:
            continue
        used[i] = True
        path.append(i)
        bat(x+1)
        path.pop()
        used[i] = False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    path = []
    used = [False for _ in range(N)]
    result = []
    bat(1)
    min_v = 10000
    for i in range(len(result)):
        line = [0] + result[i] + [0]
        sum_v = 0
        for j in range(N):
            sum_v += arr[line[j]][line[j+1]]
            if sum_v > min_v:
                break
        if min_v > sum_v:
            min_v = sum_v
    
    print(f'#{tc} {min_v}')


