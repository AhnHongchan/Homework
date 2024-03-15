T = int(input())
for tc in range(1, T+1):
    num = int(input())
    case = list(map(int, input().split()))
    min = 100000000000000
    cnt = 0
    for i in range(len(case)):
        if min > case[i]:
            min = case[i]
            cnt = i + 1
    print(f'#{tc} {cnt}')
    