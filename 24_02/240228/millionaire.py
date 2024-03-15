T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    q = [arr[N-1]]
    sum_v = 0
    for i in range(N-1, 0, -1):
        if arr[i] > q[0]:
            q.pop()
            q.append(arr[i])
        if q[0] > arr[i-1]:
            sum_v += q[0] - arr[i-1]
    print(f'#{tc} {sum_v}')
        