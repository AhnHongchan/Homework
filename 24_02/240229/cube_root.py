T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}', end=' ')
    cube = N ** (1/3)
    a = round(cube)
    if abs(a - cube) >= 0.001:
        print(-1)
    else:
        print(a)