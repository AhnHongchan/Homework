T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [-1, -1, -1, 0, 1, 1, 1, 0]
    dy = [-1, 0, 1, 1, 1, 0, -1,- 1]

    ans = 0
    for x in range(N):
        for y in range(M):
            height = arr[x][y]
            cnt = 0
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if (0 <= nx < N and 0 <= ny < M) and height > arr[nx][ny]:
                    cnt += 1
            if cnt >= 4:
                ans += 1
    print(f'#{tc} {ans}')