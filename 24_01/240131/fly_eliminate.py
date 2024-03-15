T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    blank_lst = []
    fly_cnt = 0

    for _ in range(N):
        lst = list(map(int, input().split()))
        blank_lst.append(lst)    

    for x in range(N-M+1):
        for y in range(N-M+1):
            cnt = 0
            for i in range(M):
                for j in range(M):
                    dx = x + i
                    dy = y + j
                    cnt += blank_lst[dx][dy]
                
            if cnt > fly_cnt:
                fly_cnt = cnt

    print(f'#{test_case} {fly_cnt}')

    