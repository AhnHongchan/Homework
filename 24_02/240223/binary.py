T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    print(f'#{tc}', end=' ')
    x = bin(M)
    cnt = 0
    if len(x)-2 >= N:
        for i in range(0, N):
            if M & (1<< i):
                cnt += 1
        if cnt == N:
            print('ON')
        else:
            print('OFF')        
    else:
        print('OFF')

    