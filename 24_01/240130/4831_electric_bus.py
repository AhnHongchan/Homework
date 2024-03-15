T = int(input())
for case in range(1, T+1):
    K, N, M = map(int, input().split())
    charger = list(map(int, input().split()))

    # 충전기가 있는지 정류장별로 표시
    busstop = [0] * (N + 1)
    for x in charger:
        busstop[x] = 1
    
    bus = 0 # 버스의 현재 위치
    count = 0 # 충전 횟수
    
    while bus + K < N: # 마지막 충전 이후에 도착할 수 없다면
        last = 0
        for i in range(bus+1, bus+K+1):
        # bus -> bus +K 사이의 마지막 충전기 위치 i 찾기
            if busstop[i]:      # i 정류장에 충전기가 있으면
                last = i
        # 충전기가 없으면
        if last == 0:
            count = 0
            break
        else:           # 충전기가 있으면 (운행 할 수 있는 최대 거리 이내의 마지막 충전기)
            bus = last
            count += 1
    print(f'#{case} {count}')