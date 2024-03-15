T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, -1, 0 , 1]
    dy = [-1, 0 , 1, 0]

    max_v = 0
    for x in range(N):
        for y in range(M):
            sum_v = 0
            a = arr[x][y]
            sum_v += a
            for k in range(4):
                for p in range(1, a+1):
                    nx = x + dx[k] * p
                    ny = y + dy[k] * p
                    if 0 <= nx < N and 0 <= ny < M:
                        sum_v += arr[nx][ny]

            if max_v < sum_v:
                max_v = sum_v

    print(f'#{tc} {max_v}')
