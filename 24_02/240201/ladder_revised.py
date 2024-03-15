import sys
sys.stdin = open("input.txt")

dx = [-1, 0, 0]
dy = [0, 1, -1]

T = 10
for tc in range(1, T+1):
    num = int(input())
    # 양 끝에 벽을 세워주기 위해 0 컬럼 추가: 양 끝에서 발생하는 out_of_range를 막아주기 위함이다.
    a = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]

    for j in range(102):
        if a[99][j] == 2:
            y = j

    # 방향 위로 초기화
    d = 0  # 0: 위, 1: 오, 2: 왼
    x = 99
    while True:
        # 반복문 계속 돌리다가 row 인덱스가 0 이 되면 끝내고 리턴
        if x == 0:
            break

        # 왼쪽에 1이 있으면 왼쪽으로 계속 가다가 0 나오면 반복문 종료
        if a[x][y-1] == 1:
            d = 2
            while True:
                x += dx[d]
                y += dy[d]
                if a[x][y-1] == 0:
                    break

        # 오른쪽에 1이 있으면 오른쪽으로 계속 가다가 0 나오면 반복문 종료
        elif a[x][y+1] == 1:
            d = 1
            while True:
                x += dx[d]
                y += dy[d]
                if a[x][y+1] == 0:
                    break

        # 양옆에 1 하나도 없으면 계속 직진(i.e. d=0) 또는
        # 왼쪽이든 오른쪽이든 가다가 next col에서 0이면 d=0(위)로 체인지
        d = 0
        x += dx[d]
        y += dy[d]

    print(f"#{num} {y-1}")

        

        