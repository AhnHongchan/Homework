T = int(input())
 
for test in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
 
    line = []
    max_len = 0
    line_sum = 0
    now = 0
    while now <= N-1:
        q = [arr[now]]
        now += 1
        for i in range(now, N):
            if arr[i-1] < arr[i]:
                q.append(arr[i])
                now += 1
            else:
                break
        if len(q) != 1:
            line.append(q)
            if len(q) > max_len:
                max_len = len(q)
                line_sum = sum(q)
            elif len(q) == max_len:
                if sum(q) > line_sum:
                    line_sum = sum(q)
 
    print(f'#{test} {len(line)} {line_sum}')