def postorder(root):
    global cal
    root = int(root) - 1
    nod = tree[root]            
    if len(nod) == 4:                           
        postorder(nod[2])            
        postorder(nod[3])
        cal.append(nod[1]) 
    else:
        cal.append(nod[1])
    
    return cal

for tc in range(1, 11):
    N = int(input())
    tree = [input().split() for _ in range(N)]
    cal = []
    # print(f'#{tc}', end=' ')
    result = postorder(1)

    stack = []

    for x in result:
        if x.isdigit():     # 피연산자인 경우
            stack.append(int(x))
        else:
            a = stack.pop()
            b = stack.pop()
            if x == '+':
                stack.append(b+a)
            if x == '*':
                stack.append(b*a)
            if x == '-':
                stack.append(b-a)
            if x == '/':
                stack.append(b//a)
    
    ans = stack.pop()
    print(f"#{tc} {ans}")

    
