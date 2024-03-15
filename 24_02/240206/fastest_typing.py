T = int(input())
for tc in range(1, T+1):
    A, B = input().split()
 
    N = len(A)
    M = len(B)

    cnt = 0
    i = 0       # A에서 비교 시작 위치
    j = 0       # B에서의 비교 위치
    while i<=N-M:       # B의 길이만큼인 마지막 구간의 시작 위치
        if A[i+j] == B[j]:  # 같은 글자면
            j += 1
            if j == M:      # B의 마지막 글자인 경우
                cnt += 1      # 단축키 횟수
                j = 0         # 패턴을 찾은 경우
                i += M
        else:
            j = 0
            i += 1

    print(f'#{tc} {N-M*cnt+cnt}')