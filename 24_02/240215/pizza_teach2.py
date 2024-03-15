T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))

    last = -1 # 화덕에서 마지막으로 들어간 피자 인덱스 (front)
    oven_size = N+1
    oven = [0] * oven_size
    front = rear = 0
    for i in range(N):
        rear += 1
        oven[rear] = i
        last += 1

    tmp = -1    # 치즈를 확인중인 피자(인덱스)
    while front != rear:        # 오븐(순환큐)이 비워질 때까지
        front = (front+1) % oven_size       #먼저 투입된 피자순으로 꺼내서(dequeue)
        tmp = oven[front]
        pizza[tmp] //= 2
        if pizza[tmp] > 0:      # 치즈가 남아있다면 재투입
            rear = (rear+1) % oven_size
            oven[rear] = tmp
        elif last < M:      #  치즈가 다 녹았고, 대기중인 피자(인덱스)가 있으면
            rear = (rear + 1) % oven_size
            oven[rear] = last
            last += 1         # 0으로 초기화된 경우, 투입될 피자(인덱스)
    print(f'#{tc} {tmp+1}')