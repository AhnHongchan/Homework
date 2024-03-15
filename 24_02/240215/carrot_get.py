T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    carrot_lst = list(map(int, input().split()))
    sum_carrots = 0
    for carrot in carrot_lst:
        sum_carrots += carrot
    counts = [0] * N
    min_val = 201
    min_i = 0
    tmp_sum = 0
    for i in range(0, len(carrot_lst)):
        tmp_sum += carrot_lst[i]
        counts[i] = tmp_sum
        minus_value = (sum_carrots - tmp_sum) - tmp_sum
        if minus_value < 0:
            minus_value *= (-1)
        if min_val > minus_value:
            min_val = minus_value
            min_i = i
 
    print(f'#{tc}', min_i + 1, min_val)
