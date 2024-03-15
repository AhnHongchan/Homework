T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    lst = []
    ans = 'no'

    for x in range(N):
        for y in range(N):
            if arr[x][y] == '#':
                lst.append([x, y])

    length = len(lst) ** 0.5
    if length.is_integer():
        a, b = lst.pop(0)
    
        for x in range(a, a + int(length)):
            for y in range(b, b+ int(length)):
                if arr[x][y] == '#':
                    ans = 'yes'
                else:
                    ans = 'no'
                    break
            if ans == 'no':
                break
    print(f'#{tc} {ans}')