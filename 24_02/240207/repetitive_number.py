T = int(input())
for tc in range(1, T+1):
    case = list(input())

    i = 0
    while i <= len(case) -2:
        if case[i] == case[i+1]:
            case.pop(i)
            case.pop(i)
            i = 0
        else:
            i += 1
    
    print(f"#{tc} {len(case)}")