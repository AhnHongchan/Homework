def f(N):
    for x in range(N):
        for y in range(N):
            if arr[x][y] == 'o':                
                for i in range(4):
                    cnt = 1
                    for j in range(1, 5):
                        nx = x + dx[i] * j
                        ny = y + dy[i] * j
                        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 'o':
                            cnt += 1
                    if cnt == 5:
                        return 'YES'
                    
    return 'NO'                    

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    dx = [0, 1, 1, -1]
    dy = [1, 0, 1, 1]

    print(f'#{tc} {f(N)}')
