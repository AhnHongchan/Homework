for test_case in range(1, 11):
    num = int(input())
    blank_lst = []

    for _ in range(100):
        lst = list(map(int, input().split()))
        blank_lst.append(lst)
    
    sum_ver = 0
    sum_hor = 0
    sum_left_cross = 0
    sum_right_cross = 0
    
    for y in range(100):
        ex_ver = 0
        for x in range(100):
            ex_ver += blank_lst[x][y]
        
        if sum_ver < ex_ver:
            sum_ver = ex_ver

    for x in range(100):
        ex_hor = 0
        for y in range(100):
            ex_hor += blank_lst[x][y] 
        
        if sum_hor < ex_hor:
            sum_hor = ex_hor


    ex_left_cross = 0

    for x in range(100):
        ex_left_cross += blank_lst[x][x]
    
    if sum_left_cross < ex_left_cross:
        sum_left_cross = ex_left_cross
    
    ex_right_cross = 0
    for x in range(100):
        ex_right_cross += blank_lst[x][99-x]
    
    if sum_right_cross < ex_right_cross:
        sum_right_cross = ex_right_cross
    
    max_lst = [sum_ver, sum_hor, sum_left_cross, sum_right_cross]
    max_val = 0
    for i in max_lst:
        if max_val <= i:
            max_val = i

    print(f'#{num} {max_val}')
