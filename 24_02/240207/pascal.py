T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * i for i in range(1, N+1)]

    arr[0][0] = 1
    for i in range(N):
        arr[i][0] = arr[i][-1] = 1

    for i in range(1, N-1):
        for j in range(0, i):
            arr[i+1][j+1] = arr[i][j] + arr[i][j+1]

    print(f"#{tc}")
    for i in range(N):
        print(*arr[i])
