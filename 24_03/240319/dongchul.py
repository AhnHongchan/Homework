def dfs(level, mul_v):
    global max_v
    if level == N:
        if max_v < mul_v:
            max_v = mul_v
        return
    
    if max_v >= mul_v:
        return
    
    for j in range(N):
        if path[j] == 0:
            path[j] = 1
            dfs(level + 1, mul_v * arr[level][j]*0.01)
            path[j] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    path = [0] * N
    max_v = 0

    dfs(0, 1)
    print(f'#{tc} {100 * max_v:.6f}')