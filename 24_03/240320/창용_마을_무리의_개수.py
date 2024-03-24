def find_set(x):
    if x == parents[x]:
        return x
    return find_set(parents[x])

def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x != root_y:
        parents[root_y] = root_x
    return True

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    nodes = [i for i in range(1, N + 1)]
    parents = [i for i in range(N + 1)]

    for _ in range(M):
        n1, n2 = map(int, input().split())
        union(n1, n2)

    root = set()
    for node in nodes:
        root.add(find_set(node))

    print(f'#{tc} {len(root)}')