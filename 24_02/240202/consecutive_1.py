T = int(input())
for tc in range(1, T+1):
    length = int(input())
    line = list(map(int, input()))

    i = 0
    sum = 0
    cnt = 0

    while i <= length-1:
        if line[i] == 1:
            if i <length-1:
                cnt += 1
                i += 1
            else:
                cnt += 1
                i += 1
                if sum <= cnt:
                    sum = cnt
                    cnt = 0

        else:
            i += 1
            if sum <= cnt:
                sum = cnt
                cnt = 0

    
    print(f"#{tc} {sum}")

            