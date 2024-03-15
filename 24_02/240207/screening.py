#괄호가 짝을 이뤘는지 검사 프로그램
#짝 이루면 1, 아니면 0출력
 
T = int(input())
for tc in range(1, T+1):
    String = input() #문자열 입력
    n = len(String) #문자열 길이
    stack = [0]*(n+1)
    top = -1
    for str_ in String:
        if str_ == '{':
            top += 1
            stack[top] = '{'
        elif str_ == '(':
            top += 1
            stack[top] = '('
        elif str_ == '}':
            top -= 1
            if stack[top+1] == '{':
                pass
            else:
                print(f'#{tc} 0')
                break
 
        elif str_ == ')':
            top -= 1
            if stack[top+1] == '(':
                pass
            else:
                print(f'#{tc} 0')
                break
    else:
        if top == -1:
            print(f'#{tc} 1')
        else:
            print(f'#{tc} 0')
