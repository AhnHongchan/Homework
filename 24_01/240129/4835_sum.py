a = int(input())

for i in range(1, a+1):
    b, c = map(int, input().split())
    d = list(map(int, input().split()))
    max_num = 0
    min_num = 1000000000
    for j in range(b - c + 1):
        range_list = d[j:j+c]
        result = sum(range_list)    
        if max_num < result:
                max_num = result
        if min_num > result:
                min_num = result

    print(f'#{i} {max_num - min_num}')