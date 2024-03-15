T = int(input())
for tc in range(1, T+1):
    arr = list(input())
    cnt = 0
    for i in range(len(arr)):
        if arr[i] == '(':
                cnt += 1
        elif arr[i] == ')':
            cnt += 1
            if 0 <= i-1 < len(arr)-1:
                if arr[i-1] == '(':
                    cnt -= 1
    print(f'#{tc} {cnt}')