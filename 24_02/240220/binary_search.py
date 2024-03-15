def inorder_traverse(T):            # 중위순회
    global cnt, N
    if T > N:
        return 0
    if T:                           # T is not None
        inorder_traverse(T*2)
        arr[T] = cnt
        cnt += 1                
        inorder_traverse(T*2+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 1
    arr = [0] * (N+1)
    inorder_traverse(1)
    print(f'#{tc} {arr[1]} {arr[N//2]}')

