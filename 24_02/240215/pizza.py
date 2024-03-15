T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    cheese = []

    for i in range(M):
        cheese.append([arr[i], i])

    firepot = cheese[:N]
    rest = cheese[N:]
    
    while len(firepot) > 1:
        pizza = firepot.pop(0)
        pizza[0] //= 2
        if pizza[0] == 0:
            if rest:
                firepot.append(rest.pop(0))
        else:
            firepot.append(pizza)
    
    print(f'#{tc} {firepot[0][1] + 1}')


        