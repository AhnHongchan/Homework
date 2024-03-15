T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    for _ in range(M):
        i, j = map(int, input().split())
        for k in range(j):
            if 0 <= i-1+k < N:
                if arr[i-1]:
                    arr[i-1+k] = 1
                else:
                    arr[i-1+k] = 0
    print(f'#{tc}', *arr)
