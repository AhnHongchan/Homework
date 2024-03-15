T = int(input())
for i in range(1, T+1):
    test_case = int(input())
    ex = list(map(int, input().split()))
    max_num = ex[0]
    min_num = ex[0]
    pos_max = 0
    pos_min = 0
    for m in range(len(ex)):
        if max_num <= ex[m]:
            max_num = ex[m]
            pos_max = m

    for n in range(len(ex)):        
        if min_num > ex[n]:
            min_num = ex[n]
            pos_min = n
    
        
    print(f'#{i} {abs(pos_max - pos_min)}')
