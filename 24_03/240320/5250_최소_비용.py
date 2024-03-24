from collections import deque

def find():
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    Height = 1000
    distance = [[Height] * N for _ in range(N)]    # 최단거리 배열
    distance[0][0] = 0  # 시작 값을 0으로
    q = deque()
    q.append((0,0))
    while q:
        idx = q.popleft()
        for k in range(4):
            nx = idx[0] + dx[k]
            ny = idx[1] + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                diff = 0    # 높이 차이
                if arr[nx][ny] > arr[idx[0]][idx[1]]: # 현재보다 가는 곳의 높이가 더 높은 경우
                    diff = arr[nx][ny] - arr[idx[0]][idx[1]] # 높이 차이를 갱신해준다.
                
                if distance[nx][ny] > distance[idx[0]][idx[1]] + diff + 1: 
                    # 내가 가려던 곳에 현재 값에 높이 차이와 1(이동 값)을 더한 것보다 
                    # 더 큰 값이 저장된 경우
                    # 즉 distance[nx][ny]에 최소값이 들어 있지 않은 경우 갱신
                    distance[nx][ny] = distance[idx[0]][idx[1]] + diff + 1
                    q.append((nx, ny))
    return distance[N-1][N-1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {find()}')