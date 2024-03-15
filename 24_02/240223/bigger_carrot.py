T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    result = []
    cnt = 1
    for i in range(N-1):
        if lst[i] < lst[i+1]:
            cnt += 1
        else:
            result.append(cnt)
            cnt = 1
    result.append(cnt)
    
    print(f'#{tc} {max(result)}')