def pole():
    cnt = 0
    for i in range(N):
        for j in range(i):
            std_x, std_y = arr[i][0], arr[i][1]
            tar_x, tar_y = arr[j][0], arr[j][1]
            if std_y < tar_y:
                cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for x in range(N):
        arr[x][0]
    
    arr.sort(key = lambda x:x[0])
    result = pole()
    print(f'#{tc} {result}')