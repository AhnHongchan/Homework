# 2. BFS 관련 문제

"""
V E: V 1 ~ V번까지 V개의 정점. E개의 간선
E개의 간선정보
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""

def bfs(s, N, G):           # 시작정점 s, 노드개수 N
    q = []
    visited = [0] * (N+1)  # 큐 생성
    q.append(s)             # visited 생성
    visited[s] = 1         # 시작점 enQueue
    while q:                # 처리안된 정점이 남아있으면,
        t = q.pop(0)               # 처리할 정점 dequeue 
        if t == G: 
            return visited[t] - 1  # 최단 경로 간선 수
        for i in adjl[t]:          # t의 인접 정점이
            if visited[i] == 0:                 # enQueue되지 않았으면(처리된 적이 없으면)
                q.append(i)
                visited[i] = visited[t] + 1
    return 0       # G까지 경로가 없는 경우

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())

    adjl = [[] for _ in range(V+1)]
    for i in range(E):
        n1, n2 = map(int, input().split())
        adjl[n1].append(n2)
        adjl[n2].append(n1) # 무향그래프
        """
        [[],
        [2,3],
        [4,5]...]
        """
    S, G = map(int, input().split())
    print(f'#{tc} {bfs(S, V, G)}')