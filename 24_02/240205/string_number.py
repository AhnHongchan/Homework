T = int(input())
for tc in range(1, T+1):
    str_1 = input()
    str_2 = input()
    result = [0] * len(str_1)
    
    for i in range(len(str_1)):
        for j in range(len(str_2)):
            if str_1[i] in str_2[j]:
                result[i] += 1
    
    max = result[0]
    for k in range(len(result)):
        if max <= result[k]:
            max = result[k]
    
    print(f"#{tc} {max}")
