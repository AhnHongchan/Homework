def enq(n):
    global last
    last += 1       # 마지막 노드 추가(완전이진트리 유지)
    h[last] = n     # 마지막 노드에 데이터 삽입
    c = last        # 부모 < 자식 (c는 현재 위치)
    p = c//2        # 부모번호 계산 (p는 부모의 위치)
    while p >= 1 and h[p] > h[c]:     # 부모가 있는데, 더 크면
        h[p], h[c] = h[c], h[p]     # 교환
        c = p
        p = c // 2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    h = [0] * (N+1)
    last = 0 # 힙의 마지막 노드 번호
    print(f'#{tc}', end = ' ')
    for i in range(len(lst)):
        enq(lst[i])
    
    sum_val = 0
    while N >= 1:
        N = N // 2
        sum_val += h.pop(N)
    
    print(sum_val)
