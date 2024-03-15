T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    for i in range(N):
        for j in range(M):
            sum_v = 0
            k = arr[i][j]
            sum_v += arr[i][j]
            for x in range(1, k+1):
                if 0 <= i-x < N:
                    sum_v += arr[i-x][j]
                if 0 <= i+x < N:
                    sum_v += arr[i+x][j]
                if 0 <= j-x < N:
                    sum_v += arr[i][j-x]
                if 0 <= j+x < M:
                    sum_v += arr[i][j+x]

            if max_v < sum_v:
                max_v = sum_v
    
    print(f'#{tc} {max_v}')
                