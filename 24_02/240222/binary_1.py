def f(x):
    if x//2 == 0:
        return str(x%2)
    return f(x//2)+str(x%2)


T = int(input())
for tc in range(1, T+1):
    N, lst = input().split()
    lst = list(lst)
    print(f'#{tc}', end=' ')
    for x in lst:
        if x.isalpha():
            x = ord(x)-55
        x = int(x)
        result = f(x)
        while len(result) < 4:
            result = '0' + result
        print(f'{result}', end='')
    print()
    