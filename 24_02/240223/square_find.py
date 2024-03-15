T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = []
    dx = [0, 1]
    dy = [1, 0]
    cnt = 0
    for x in range(N):
        for y in range(N):
            if arr[x][y] == 1:
                for j in range(N):
                    nx = x + j
                    for k in range(N):
                        ny = x + k
                        if 0 <= nx < N and 0 <= ny < N:
                            if arr[nx][ny] == 1:
                                cnt += 1
                            elif arr[nx][y] == 0:
                                result.append(cnt)
                                cnt = 0
    result.append(cnt)            

    print(f'#{tc} {max(result)}')