T = int(input())
for tc in range(1, T+1):
    arr = input().split()
    stack = []
    ans = 0

    for x in arr:
        if x.isdigit():     # 피연산자인 경우
            stack.append(int(x))
        elif x == '.':
            if len(stack) == 1:
                ans = stack.pop()
                break
            else:
                ans = 'error'
                break
        else:
            if len(stack) == 1:
                ans = 'error'
                break
            else:
                a = stack.pop()
                b = stack.pop()
                if x == '+':
                    stack.append(b+a)
                if x == '-':
                    stack.append(b-a)
                if x == '*':
                    stack.append(b*a)
                if x == '/':
                    stack.append(int(b/a))
                
    
    print(f"#{tc} {ans}")
            
            

        