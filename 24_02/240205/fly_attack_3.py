T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    case = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 1, 0, -1, -1, 1, 1, -1]
    dy = [1, 0, -1, 0, -1,- 1, 1, 1]
    max_sum = 0

    for x in range(N):
        for y in range(N):
            sum = case[x][y]
            cross = case[x][y]
            best = 0
            for a in range(1, M):
                for z in range(8):
                    nx = x + dx[z] * a
                    ny = y + dy[z] * a
                    if (0 <= nx <= N-1 and 0 <= ny <= N-1):
                        if z < 4:
                            sum += case[nx][ny]
                        else:
                            cross += case[nx][ny]
            if sum >= cross:
                best = sum
            else:
                best = cross

            if max_sum <= best:
                max_sum = best

    print(f"#{tc} {max_sum}")