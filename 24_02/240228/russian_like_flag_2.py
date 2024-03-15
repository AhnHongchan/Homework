T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    ans = N * M
    
    for i in range(0, N - 2):
        white = sum(1 for j in range(M) if arr[i][j] != 'W')
        
        for k in range(i + 1, N - 1):
            blue = sum(1 for j in range(M) if arr[k][j] != 'B')
            red = sum(1 for j in range(M) if arr[k + 1][j] != 'R')

            change = white + blue + red
            ans = min(ans, change)

    print(f'#{tc} {ans}')
