T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    point = M % N
    print(f'#{tc} {arr[point]}')