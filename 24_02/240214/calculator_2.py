top = -1
stack = [0] * 100

icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}      # 스택 밖에서의 우선순위
isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}      # 스택 안에서의 우선순위

for tc in range(1, 11):
    num = int(input())
    fx = '(' + input() + ')'
    postfix = ''

    for tk in fx:
        if tk == '(' or (tk in '*/+-' and isp[stack[top]] < icp[tk]):       
            top += 1     # push
            stack[top] = tk

        elif tk in '*/+-' and isp[stack[top]] >= icp[tk]:   # 연산자이고 top 원소보다 우선순위가 높지 않은 경우
            while isp[stack[top]] >= isp[tk]:       # top 원소보다 우선순위가 낮을 때까지
                top -= 1    # pop
                postfix += stack[top+1]
            top += 1
            stack[top] = tk

        elif tk == ')':
            while stack[top] != '(':
                top -= 1    # pop
                postfix += stack[top+1]
            top -= 1    # 여는 괄호 pop해서 버림
        else:
            postfix += tk
    
    stack2 = []
    ans = 0

    for x in postfix:
        if x.isdigit():     # 피연산자인 경우
            stack2.append(int(x))
        else:
            a = stack2.pop()
            b = stack2.pop()
            if x == '+':
                stack2.append(b+a)
            if x == '*':
                stack2.append(b*a)
    
    ans = stack2.pop()
                
    print(f"#{tc} {ans}")