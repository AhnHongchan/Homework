T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    A = B = C = D = 0
    
    for x in range(N):
        for y in range(N):
            if x < N // 2 and x < y < N - x:
                A += arr[x][y]
            if y > N // 2 and N-y <= x < y:
                B += arr[x][y]
            if x > N//2 and N-x <= y < x:
                C += arr[x][y]
            if y < N // 2 and y < x < N-y:
                D += arr[x][y]
    print(f'#{tc}', max(A,B,C,D) - min(A,B,C,D))