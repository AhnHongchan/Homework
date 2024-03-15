def snack(lev, start):
    global result
    if lev == 2:
        if sum(path) > M:
            return
        else:
            result.append(sum(path))
            return

    for i in range(start, N):
        path.append(arr[i])
        snack(lev+1, i+1)
        path.pop()

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    
    path = []
    result = []
    snack(lev = 0, start = 0)

    if result:
        ans = max(result)
    else:
        ans = -1
    print(f'#{tc} {ans}')