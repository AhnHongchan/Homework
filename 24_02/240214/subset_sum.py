def f(i, M, N, K, c, s):    # c 부분집합 원소 개수, s 부분집합의 합
    global cnt
    if N == c and K == s:
        cnt += 1
    elif i == M:
        return
    elif s > K or c > N:    # 부분집합의 합이 목표보다 크거나 더 많은 원소가 선택된 경우
        return
    else:
        f(i+1, M, N, K, c + 1, s + arr[i])  # arr[i]가 포함되는 경우
        f(i+1, M, N, K, c, s)           # arr[i]가 포함되지 않는 경우
 
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())    # 원소의 개수 N, 합 K
    arr = [i for i in range(1, 13)]
    cnt = 0
    f(0, 12, N, K, 0, 0)
    print(f'#{tc} {cnt}')