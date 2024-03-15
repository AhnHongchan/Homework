T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    max_v = 0
    for x in range(N):
        for y in range(N):
            sum_v = 0
            sum_v += arr[x][y]
            for i in range(4):
                for j in range(1, N):
                    nx = x + dx[i] * j
                    ny = y + dy[i] * j
                    if 0 <= nx < N and 0 <= ny < N:
                        sum_v += arr[nx][ny]
            if max_v < sum_v:
                max_v = sum_v

    print(f'#{tc} {max_v}')