def f(p):
    c = p * 2
    if c <= N:
        if c + 1 <= N:
            return f(c) + f(c+1)
        else:
            return f(c)
    else:
        return h[p]

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    h = [0] * (N+1)
    for _ in range(M):
        idx, val = map(int, input().split())
        h[idx] = val

    result = f(L)
    print(f'#{tc} {result}')
    
