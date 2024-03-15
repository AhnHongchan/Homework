def max_sort(x, N):
    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if x[j] < x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
        if i > b:
            break
        

T = int(input())

for tc in range(1, T+1):
    a, b = map(int, input().split())
    lst = []
    while True:
        if a // 10 != 0:
            lst.append(a % 10)
            a //= 10
        else:
            lst.append(a)
            break

    lst.reverse()
    max_sort(lst, len(lst))

    print(f"#{tc}", end=" ")
    print(*lst, sep="")
    



            


    