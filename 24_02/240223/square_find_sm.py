t = int(input())
for test_case in range(1, t + 1):
    n = int(input())
    rect_map = [list(map(int, input().split())) for _ in range(n)]
 
    result = 0
    for i in range(n):
        for j in range(n):
            if rect_map[i][j] == 1:
                ni = i
                nj = j
                count_row = 0
                count_col = 0
                while 0 <= ni < n and rect_map[ni][j] != 0:
                    ni += 1
                    count_row += 1
                while 0 <= nj < n and rect_map[i][nj] != 0:
                    nj += 1
                    count_col += 1
                sum = count_row * count_col
                if result < sum:
                    result = sum
 
    print(f'#{test_case} {result}')