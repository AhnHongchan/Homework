T = int(input())
lst = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for tc in range(1, T+1):
    a, b = map(str, input().split())
    b = int(b)
    c = list(input().split())

    result =[]

    for num in lst:
        for i in range(len(c)):
            if c[i] == num:
                result += [num]
    
    print(f"#{tc}")
    print(*result)

    



