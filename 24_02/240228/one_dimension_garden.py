T = int(input())
for tc in range(1, T+1):
    N, D = map(int, input().split())
    water = 1 + 2 * D
    if N % water == 0:
        cnt = N // water
    else:
        cnt = (N // water) + 1
    print(f'#{tc} {cnt}')
