T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    min_val = 10000

    for i in range(N-1):
        for j in range(N-1):
            diff = 0
            A = B = C = D = 0
            for p in range(N):      # 영역을 바꿀 때마다 모든 칸을 순회
                for q in range(N):
                    if p <= i and q <= j:
                        A += arr[p][q]
                    elif p <= i and q > j:
                        B += arr[p][q]
                    elif p > i and q <= j:
                        C += arr[p][q]
                    else:
                        D += arr[p][q]
            
            diff = max(A,B,C,D) - min(A,B,C,D)
            if min_val > diff:
                min_val = diff
    print(f'#{tc} {min_val}')