T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    for x in range(N):
        for y in range(M):
            if arr[x][y] == 1:
                cnt = 1
                for k in range(1, N):
                    nx = x + k
                    if 0 <= nx < N and arr[nx][y] == 1:
                        cnt += 1
                    else:
                        break
                if max_v < cnt:
                    max_v = cnt
                
                cnt = 1
                for l in range(1, M):
                    ny = y + l
                    if 0 <= ny < M and arr[x][ny] == 1:
                        cnt += 1
                    else:
                        break
                if max_v < cnt:
                    max_v = cnt
    print(f'#{tc} {max_v}')

