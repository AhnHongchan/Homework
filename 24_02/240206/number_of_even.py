T = int(input())
for tc in range(1, T+1):
    num = int(input())
    case = list(map(int, input().split()))
    cnt = 0

    for number in case:
        if number % 2 == 0:
            cnt += 1
    
    print(f'#{tc} {cnt}')
