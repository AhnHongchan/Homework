T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
 
    #bit(N-1) - bit0이 모두 1인 숫자
    b = (1<<N) -1 #N=4인 경우 00001111 (1<<4) -1
    if M&b == b:
        print(f'#{tc} ON')
    else:
        print(f'#{tc} OFF')