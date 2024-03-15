T = int(input())
 
 
def dfs(i):
    visited[i] = 1
    st = []
    while True:
        # 인접 리스트를 돌면서, 방문처리를 하고,
        # 이전에 방문한 장소를 스택에 어펜드 처리를 한다.
        for l in adj_li[i]:
            # 만약 인접한 장소가 방문 이력이 없다면
            if visited[l] == 0:
                # 지금 위치를 스택에 push하고
                st.append(i)
                # 인접한 장소로 이동한다.
                i = l
                # 그 뒤, 이동한 장소를 방문 처리한다.
                visited[l] = 1
                break
        # 만약 반복문이 정상적으로 종료된다면
        # 아래 코드를 실행한다.
        else:
        # 스택에 값이 남아있다면
        # 이전 위치로 뒷걸음질
            if st:
                i = st.pop()
        # 스택에 값이 남아있지 않다면
        # 반복문 종료
            else:
                break
 
 
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj_li = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    for _ in range(E):
        n1, n2 = map(int, input().split())
        adj_li[n1].append(n2)
    start, end = map(int, input().split())
 
    dfs(start)
    print(f'#{tc} {visited[end]}')