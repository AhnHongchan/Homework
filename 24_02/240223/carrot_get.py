T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    sum_v = 1000000
    for i in range(N):
        left = sum(lst[:i])
        right = sum(lst[i:])
        diff = abs(right - left)
        if sum_v > diff:
            sum_v = diff
            idx = i
    print(f'#{tc} {idx} {sum_v}')