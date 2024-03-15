T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    max_v = 0

    for x in range(N-M+1):
        for y in range(N-M+1):
            sum_v = 0
            for j in range(M):
                nx = x + j
                for k in range(M):
                    ny = y + k
                    sum_v += arr[nx][ny]
            if max_v < sum_v:
                    max_v = sum_v

    print(f'#{tc} {max_v}')

            