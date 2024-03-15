T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cont = list(map(int, input().split()))
    cont.sort(reverse = True)
    truck = list(map(int, input().split()))
    truck.sort(reverse = True)
    
    weight = 0
    i = 0
    cnt = 0
    while i <= M-1:
        for j in range(cnt, N):
            if truck[i] >= cont[j]:
                weight += cont[j]
                cnt = j+1
                break
        i += 1
    
    print(f'#{tc} {weight}')