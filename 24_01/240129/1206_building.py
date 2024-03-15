for i in range(1, 11):
    num = int(input())
    building = list(map(int, input().split()))
    cnt = 0
    for j in range(2, num-2):
        height = building[j]
        range_list = building[j-2:j] + building[j+1:j+3]
        max_num = 0
        for k in range_list:
            if max_num < k:
                max_num = k                
        if height > max_num:
            cnt += height - max_num        
    print(f'#{i} {cnt}')
