T = int(input())
for tc in range(1,T+1):
    arr = list(map(int, input().split()))
    N, M = arr[0], arr[1:]
    i = 0
    cnt = 0
    while i + M[i] < N-1:
        max_nxt = 0
        idx = i
        for j in range(i+1, i+M[i]+1):
            nxt = j + M[j]
            if max_nxt < nxt:
                max_nxt = nxt
                idx = j
        i = idx
        cnt += 1
    
    print(f'#{tc}', cnt)