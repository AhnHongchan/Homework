def binarySearch(target):
    left = 0
    right = len(lst_a)-1
    check = 2
    while left <= right:
        mid = (left+right)//2
        if lst_a[mid] == target:
            return 1
        elif lst_a[mid] < target:
            left = mid+1
            if check == 1:
                return 0
            else: check = 1
        else:
            right = mid-1
            if check == 0:
                return 0
            else: check = 0
    return 0

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst_a = list(map(int, input().split()))
    lst_b = list(map(int, input().split()))
    lst_a.sort()
    cnt = 0
    for x in lst_b:
        result = binarySearch(x)
        if result:
            cnt += 1
    
    print(f'#{tc} {cnt}')