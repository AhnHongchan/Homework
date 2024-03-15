import sys
sys.stdin = open("input.txt")

dx = [1, 0, 0]
dy = [0, 1, -1]

T = 10
for tc in range(1, T+1):
    num = int(input())
    # 양 끝에 벽을 세워주기 위해 0 컬럼 추가: 양 끝에서 발생하는 out_of_range를 막아주기 위함이다.
    a = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]

    # for j in range(102):
    #     if a[99][j] == 2:
    #         y = j


    d = 0  # 0: 위, 1: 오, 2: 왼
    x = 0
    y = 1
    while True:

        if x == 99 and a[x][y] == 2:
            break


        if a[x][y-1] == 1:
            d = 2
            while True:
                x += dx[d]
                y += dy[d]
                if a[x][y-1] == 0:
                    break


        elif a[x][y+1] == 1:
            d = 1
            while True:
                x += dx[d]
                y += dy[d]
                if a[x][y+1] == 0:
                    break

        d = 0
        x += dx[d]
        y += dy[d]

    print(f"#{num} {y-1}")

        

        