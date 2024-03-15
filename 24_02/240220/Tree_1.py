def subtree(a):
    global cnt
    if left[a]:
        subtree(left[a])
    if right[a]:
        subtree(right[a])
    cnt += 1

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    left = [0] * (E+2)          # 부모가 자식을 인덱스로 저장
    right = [0] * (E+2)
    par = [0] * (E+2)           # 자식을 인덱스로 부모 저장

    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]
        if left[p] == 0:        # 왼쪽 자식이 없으면
            left[p] = c
        else:
            right[p] = c
        par[c] = p
    
    cnt = 0
    subtree(N)

    print(f'#{tc} {cnt}')
