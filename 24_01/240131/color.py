# import numpy as np
T = int(input())

for test_case in range(1, T + 1):
    num = int(input())
    blank_lst = [[0 for _ in range(10)] for _ in range(10)]
    
    for _ in range(num):
        x1, y1, x2, y2, color = map(int, input().split())

        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                blank_lst[i][j] += color

    cnt = 0
    
    for x in range(10):
        for y in range(10):
            if blank_lst[x][y] == 3:
                cnt += 1
    
    print(f'#{test_case} {cnt}')