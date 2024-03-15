# 피자 굽기
"""
화덕에 N개의 피자를 구울 수 있음
1~M번까지 피자
조건
한 바퀴 돌때 녹지않은 치즈의 양은 반으로 줄어듦
C -> C//2
0이 될때 화덕에서 꺼낼것
"""
 
 
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    # 원형 큐 생성
    rear = 0
    q = [0] * N
    i = 0
    total_pizza = M
    while total_pizza != 0:
        if q[rear] == 0:
            if i != M:
                pizza = [i+1, arr[i]]
                q[rear] = pizza
                i += 1
        else:
            q[rear][1] //= 2
            if q[rear][1] == 0:    # 피자 꺼냄
                total_pizza -= 1
                if total_pizza == 0:
                    print(f'#{t} {q[rear][0]}')
                q[rear] = 0
                continue
        rear = (rear + 1) % N