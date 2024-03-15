T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    idx = []

    for x in range(10):
        for y in range(10):
            if arr[x][y] == 1:
                idx.append([x, y])
    
    a = idx.pop(0)
    b = idx.pop()

    cnt = 0
    for x in range(N):
        for y in range(N):
            if x <= a[0] and y <= a[1]:
                arr[x][y] += 3
                if arr[x][y] == 5:
                    cnt += 1
            elif x <= a[0] and y >= b[1]:
                arr[x][y] += 3
                if arr[x][y] == 5:
                    cnt += 1
            elif x >= b[0] and y <= a[1]:
                arr[x][y] += 3
                if arr[x][y] == 5:
                    cnt += 1
            elif x >= b[0] and y >= b[1]:
                arr[x][y] += 3
                if arr[x][y] == 5:
                    cnt += 1
            else:
                pass
    print(f'#{tc} {cnt}')
