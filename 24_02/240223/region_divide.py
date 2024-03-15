T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 10000000000
    for x in range(N-1):
        for y in range(N-1):
            A = B = C = D = 0
            sum_v = 0
            for i in range(x+1):
                nx = i
                for j in range(y+1):
                    ny = j
                    A += arr[nx][ny]
                for j in range(y+1, N):
                    ny = j
                    B += arr[nx][ny]
            for i in range(x+1, N):
                nx = i
                for j in range(y+1):
                    ny = j
                    C += arr[nx][ny]
                for j in range(y+1, N):
                    ny = j
                    D += arr[nx][ny]
            sum_v = max(A, B, C, D) - min(A, B, C, D)
            if result > sum_v:
                result = sum_v
    print(f'#{tc} {result}')