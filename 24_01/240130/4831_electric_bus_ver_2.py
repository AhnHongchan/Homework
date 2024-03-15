T = int(input())
for case in range(1, T+1):
    K, N, M = map(int, input().split())
    charger = [0]+list(map(int, input().split()))+ [N]  # 충전기 위치, 0은 시점 / N은 종점

    last = 0        # 마지막 충전 위치, 초기값은 출발점 0
    count = 0        # 충전 횟수
    for i in range(1, M+2):         # 모든 충전기 위치 charger[i]에 대해
        if charger[i] - charger[i- 1] <= K:     # 첫 번째 조건 충족: 충전기 사이 운행 가능
            if (charger[i] - last) > K:    # 마지막 충전기에서 너무 멀면
                last = charger[i-1]
                count += 1
        else:
            count = 0   # 중간까지 진행됐을 가능성이 있으므로 초기화한다.
            break

    print(f'#{case} {count}')
