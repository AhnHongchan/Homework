def f(x):
    y = [0] * 7
    for i in range(7):
        y[i] = int(x[i]) * (2 ** (6-i))

    sum_v = 0
    for j in range(7):
        sum_v += y[j]

    return sum_v

T = int(input())
for tc in range(1,T+1):
    binary = input()
    print(f'#{tc}', end= ' ')
    for i in range(0, len(binary), 7):
        x = binary[i:i+7]
        ans = f(x)
        print(ans, end=' ')
    print()
