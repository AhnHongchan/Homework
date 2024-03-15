T = int(input())
for tc in range(1, T+1):
    num = int(input())
    arr = [[0]*num for i in range(num)]
 
    # 방향 설정
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direction = 0
 
    # 첫 list 설정
    arr[0] = ([i for i in range(1, num+1)]) # 1~c
    value = num+1  # 초기값
    num -= 1
 
    # 좌표 설정
    x = num
    y = 0
 
    while num > 0:
        for i in range(2):
            for j in range(num):
                x = x + dx[direction]
                y = y + dy[direction]
                arr[y][x] = value
                value += 1
            direction = (direction + 1) % 4
        num -= 1
 
    print(f'#{tc}')
    for i in arr:
        print(*i)