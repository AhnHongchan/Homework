def cover(x, y):
    for m in range(3):
        if arr[x][y] == station[m]:
            for k in range(4):
                for n in range(1, m+2):
                    nx = x + dx[k] * n
                    ny = y + dy[k] * n
                    if 0 <= nx < N and 0 <= ny < N:
                        arr[nx][ny] = 'X'

T = int(input())
station = ['A', 'B', 'C']
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    for x in range(N):
        for y in range(N):
            cover(x, y)

    cnt = 0
    for lst in arr:
        for x in lst:
            if x == 'H':
                cnt += 1
    
    print(f'#{tc} {cnt}')