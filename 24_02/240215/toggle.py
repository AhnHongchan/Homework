T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0] * (N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

    toggle = [0, 1]
    k = 1
    while k <= M:
        if M % k == 0:
            for i in range(1, N+1):
                for j in range(1, N+1):
                    if arr[i][j] == toggle[0]:
                        arr[i][j] = toggle[1]
                    elif arr[i][j] == toggle[1]:
                        arr[i][j] = toggle[0]
        
        else:
            for i in range(1, N+1):
                for j in range(1, N+1):
                    if (i + j) == k or (i + j) % k == 0:
                        if arr[i][j] == toggle[0]:
                            arr[i][j] = toggle[1]
                        elif arr[i][j] == toggle[1]:
                            arr[i][j] = toggle[0]
        k += 1

    cnt = 0
    for lst in arr:
        for x in lst:
            if x == toggle[1]:
                cnt += 1
    
    print(f'#{tc} {cnt}')
