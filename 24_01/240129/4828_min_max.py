a = int(input())

for i in range(1, a+1):
    b = int(input())
    c = list(map(int, input().split()))
    max = c[0]
    min = c[0]
    for j in c:
        if j > max:
            max = j
        if j < min:
            min = j
    print(f'#{i} {max - min}')