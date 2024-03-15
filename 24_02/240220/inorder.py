def inorder(root):
    root = int(root) - 1
    nod = tree[root]            
    if len(nod) == 4:                           
        inorder(nod[2])
        print(nod[1], end='')             
        inorder(nod[3])
    elif len(nod) == 3:
        inorder(nod[2])
        print(nod[1], end='')
    else:
        print(nod[1], end='')

for tc in range(1, 11):
    N = int(input())
    tree = [input().split() for _ in range(N)]

    print(f'#{tc}', end=' ')
    inorder(1)
    print()