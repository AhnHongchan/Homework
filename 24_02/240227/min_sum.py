def min_sum(x, y, sum_v):
    global result
    if result < sum_v:
        return

    if x == N-1 and y == N-1:
        if result > sum_v:
            result = sum_v
            return
    
    dx = [1, 0]
    dy = [0, 1]

    for k in range(2):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < N:
            min_sum(nx, ny, sum_v + arr[nx][ny])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 10 * (2 * N - 1)
    min_sum(0, 0, arr[0][0])
    print(f'#{tc} {result}')

