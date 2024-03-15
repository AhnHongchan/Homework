def rectangular(a, b):
    if a[2] > b[0] and a[3] > b[1]:
        print(1)
    elif (a[2] == b[0] and a[3] > b[1] and a[1] < b[3]) or (a[3] == b[1] and a[2] > b[0] and a[0] < b[2]):
        print(2)
    elif (a[2] == b[0] and a[3] == b[1]) or (a[2] == b[0] and a[3] > b[1] and a[1] == b[3]) or (a[3] == b[1] and a[2] > b[0] and a[0] == b[2]):
        print(3)
    else:
        print(4)


T = int(input())
for tc in range(1, T+1):
    sqr1 = list(map(int, input().split()))
    sqr2 = list(map(int, input().split()))
    print(f'#{tc}', end = ' ')
    if sqr1[0] < sqr2[0]:
        rectangular(sqr1, sqr2)
    else:
        rectangular(sqr2, sqr1)