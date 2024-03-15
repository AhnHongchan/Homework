T = int(input())
for tc in range(1, T+1):
    case = list(input())
    n = len(case)
    if n % 2 == 1:
        if case[0:(n-1)//2] == case[n-1:(n-1)//2:-1]:
            print(f'#{tc}', 1)
        else:
            print(f'#{tc}', 0)
    else:
        if case[0:n//2] == case[n-1:n//2-1:-1]:
            print(f'#{tc}', 1)
        else:
            print(f'#{tc}', 0)

    
