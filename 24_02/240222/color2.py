T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    mosaic = [[0] * 10 for _ in range(10)]

    
    for i in range(N):
        a = arr[i][4]
        for j in range(arr[i][0], arr[i][2]+1):
            x = j
            for k in range(arr[i][1], arr[i][3]+1):
                y = k
                mosaic[x][y] += a

    for lst in mosaic:
        for k in lst:
            if k == 3:
                k = 0

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    sum_v = 0
    for x in range(10):
        for y in range(10):
            for k in range(1, 3):
                if mosaic[x][y] == k:
                    cnt = 4
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0 <= nx < 10 and 0 <= ny < 10:
                            if mosaic[nx][ny] == k:
                                cnt -= 1
                    sum_v += cnt

    print(f'#{tc} {sum_v}')


