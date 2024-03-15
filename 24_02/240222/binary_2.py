def f(x):
    ans = ''
    for i in range(1, 14):
        if i == 13:
            ans = 'overflow'
            break
        elif x > (1/2) ** i:
            x -= (1/2) ** i
            ans += '1'
        elif x < (1/2) ** i:
            ans += '0'
        else:
            ans += '1'
            break
        
    return ans

T = int(input())
for tc in range(1, T+1):
    n = float(input())
    print(f'#{tc} {f(n)}')
