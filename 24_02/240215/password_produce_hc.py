for _ in range(10):
    tc = int(input())
    arr = list(map(int, input().split()))

    while arr[7] != 0:
        for i in range(5):
            num = arr.pop(0)
            num -= (i+1)
            if num <= 0:
                num = 0
            arr.append(num)
            if arr[7] == 0:
                break
    
    print(f'#{tc}', *arr)
