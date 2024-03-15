def win(a, b):
    if numbers[b] - numbers[a] == 1 or numbers[b] - numbers[a] == -2:
        return b
    else:
        return a

def f(x, y):
    if x == y:
        return x
    else:
        left = f(x, (x+y)//2)
        right = f((x+y)//2+1, y)
        return win(left, right)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = [0] + list(map(int, input().split()))
    print(f'#{tc} {f(1, N)}')

    
