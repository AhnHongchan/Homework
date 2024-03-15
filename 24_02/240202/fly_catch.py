T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    max_cnt = 0

    for x in range(N-M+1):
        for y in range(N-M+1):
            sum = 0
            for i in range(M):
                for k in range(2):
                    for j in range(M):
                        for p in range(2):
                            nx = x + dx[k] * i
                            ny = y + dy[p] * j
                            sum += area[nx][ny]
            
                if max_cnt < sum:
                    max_cnt = sum

    print(sum)

