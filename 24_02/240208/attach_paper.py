def arr(N):
    a = [0] * 31
    a[1] = 1
    a[2] = 3
    for i in range(3, N+1):
        a[i] = a[i-1] + 2 * a[i-2]
    return a[N]
 
T = int(input())
for t in range(T):
    N = int(input())
    n = arr(N//10)
    print(f'#{t+1}', n)

