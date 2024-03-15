for tc in range(1, 11):
    num = int(input())
    case = [list(input()) for _ in range(8)]

    cnt = 0
    for i in range(8):
        for j in range(8-num+1):
            for k in range(num):
                if case[i][j+k] != case[i][j+num-k-1]:
                    break
            else:
                cnt += 1

    for i in range(8):
        for j in range(8-num+1):
            for k in range(num):
                if case[j+k][i] != case[j+num-k-1][i]:
                    break
            else:
                cnt += 1
    
    print(f"#{tc} {cnt}")



