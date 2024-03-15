T = int(input())
for tc in range(1, T+1):
    num = int(input())
    case = list(map(int, input().split()))
    neighbor = []
    for i in range(len(case)-1):
        neighbor.append(case[i] + case[i+1])
    
    max = neighbor[0]
    min = neighbor[0]

    for j in range(len(neighbor)):
        if max <= neighbor[j]:
            max = neighbor[j]
        if min >= neighbor[j]:
            min = neighbor[j]

    print(f'#{tc} {max} {min}')