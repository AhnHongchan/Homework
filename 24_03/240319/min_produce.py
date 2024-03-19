def dfs(level, sum_v):
    global min_v
    if level == N:
        if min_v > sum_v:
            min_v = sum_v
        return
    
    if min_v < sum_v + (N-level) * verify:
        return
    
    for j in range(N):
        if not path[j]:
            path[j] = 1
            dfs(level + 1, sum_v + arr[level][j])
            path[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    verify = min(min(*arr))
    path = [0] * N
    min_v = 1500

    dfs(0, 0)
    print(f'#{tc} {min_v}')