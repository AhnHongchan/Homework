def babygin(lst):
    global cnt
    for j in range(10):
        if lst[j] >= 3:
            lst[j] -= 3
            cnt += 1
        if j <= 7:
            if lst[j] >= 1 and lst[j+1] >= 1 and lst[j+2] >=1:
                lst[j] -= 1
                lst[j+1] -= 1
                lst[j+2] -= 1
                cnt += 1

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    print(f'#{tc}', end = ' ')
    c1 = [0] * 10
    c2 = [0] * 10
    cnt = 0
    for i in range(len(arr)):
        if i % 2 == 0:
            c1[arr[i]] += 1
            babygin(c1)
            if cnt == 1:
                print(1)
                break
        else:
            c2[arr[i]] += 1
            babygin(c2)
            if cnt == 1:
                print(2)
                break
    
    if cnt == 0:
        print(0)

    
