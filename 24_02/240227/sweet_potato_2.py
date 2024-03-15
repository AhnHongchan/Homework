T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split())) + [0]
    cnt_v = 0
    sum_v = 0
    cnt = 0
    max_cnt = 0
    node = 0
    for i in range(0, N):
        if arr[i] < arr[i+1]:
            sum_v += arr[i]
            cnt += 1
        elif arr[i] > arr[i+1] and cnt > 0:
            sum_v += arr[i]
            node += 1
            if max_cnt < cnt:
                max_cnt = cnt
                cnt_v = sum_v
                cnt = 0
                sum_v = 0
            elif max_cnt == cnt:
                max_cnt = cnt
                cnt_v = max(cnt_v, sum_v)
                cnt = 0
                sum_v = 0
 
    print(f'#{tc} {node} {cnt_v}')