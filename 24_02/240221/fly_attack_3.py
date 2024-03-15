T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 1, 0, -1, 1, -1, -1, 1]
    dy = [1, 0, -1, 0, 1, -1, 1, -1]

    max_v = 0
    for x in range(N):
        for y in range(N):
            best = 0
            sum_v = arr[x][y]                     
            cross_v = arr[x][y]
            for i in range(8):
                for j in range(1, M):
                    nx = x + dx[i] * j
                    ny = y + dy[i] * j
                    if 0 <= nx < N and 0 <= ny < N:
                        if i < 4:
                            sum_v += arr[nx][ny]
                        else:
                            cross_v += arr[nx][ny]
            if sum_v >= cross_v:
                best = sum_v
            else:
                best = cross_v
            if max_v < best:
                max_v = best
    print(f'#{tc} {max_v}')

