T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    ans = N * M
    
    white = 0
    for i in range(0, N-2):
        for j in range(M):
            if arr[i][j] != 'W':
                white += 1

        blue = 0
        for k in range(i+1, N-1):
            for j in range(M):
                if arr[k][j] != 'B':
                    blue += 1

            red = 0
            for l in range(k+1, N):
                for j in range(M):
                    if arr[l][j] != 'R':
                        red += 1

            change = white + blue + red
            if ans > change:
                ans = change

    print(f'#{tc} {ans}')