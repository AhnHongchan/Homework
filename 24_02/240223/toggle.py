T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0] * (N+1)] +[[0] + list(map(int, input().split())) for _ in range(N)]

    for k in range(1, M+1):
        if M % k == 0:
            for x in range(1, N+1):
                for y in range(1, N+1):
                    if arr[x][y]:
                        arr[x][y] = 0
                    else:
                        arr[x][y] = 1
        else:
            for x in range(1, N+1):
                for y in range(1, N+1):
                    if (x + y) % k == 0:
                        if arr[x][y]:
                            arr[x][y] = 0
                        else:
                            arr[x][y] = 1
    cnt = 0
    for lst in arr:
        for s in lst:
            if s:
                cnt += 1
    print(f'#{tc} {cnt}')
                    