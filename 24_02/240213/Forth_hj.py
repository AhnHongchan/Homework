def f(data):
    stack = []
    while True:
        datum = data.pop()  # 데이터에서 하나 꺼내기
        if datum.isdigit():  # 숫자인지 확인하고 숫자면 stack에 넣기!
            stack.append(int(datum))
        else:  # 숫자가 아니라 연산자라면!
            if datum == '.':
                if len(stack) == 1:
                    return stack[0]
                else:
                    return 'error'
            if len(stack) >= 2:  # 스택에 숫자 2개 이상 있는 경우
                a = stack.pop()
                b = stack.pop()
                if datum == '+':
                    stack.append(b+a)
                elif datum == '-':
                    stack.append(b-a)
                elif datum == '/':
                    stack.append(b//a)
                elif datum == '*':
                    stack.append(b*a)
            else:               #스택에 숫자가 2개 미만인 경우
                return 'error'
 
 
T = int(input())
for tc in range(1, 1+T):
    data = list(input().split())
    data.reverse()
    print(f'#{tc} {f(data)}')