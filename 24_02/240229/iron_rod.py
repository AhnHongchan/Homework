T = int(input())
for tc in range(T):
    data = input()
    stack = [data[0]]
    cnt = 0
    for i in range(1,len(data)):
        if data[i] == ")":
            if data[i-1] == "(":
                stack.pop()
                cnt += len(stack)
            else:
                stack.pop()
                cnt+=1
        else:
            stack.append(data[i])
    print(f"#{tc+1}",cnt)