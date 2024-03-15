for _ in range(10):
    tc = int(input())
    arr = list(map(int, input().split()))
    num = 1
    cnt = 1

    while arr[7] > 0:
            num = arr.pop(0)
            num -= cnt
            if num <= 0:
                num = 0
            cnt = (cnt % 5) + 1
            arr.append(num)
    
    print(f'#{tc}', *arr)
