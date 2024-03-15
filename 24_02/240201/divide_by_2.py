def binarysearch(N, key):
    start = 1
    end = N
    cnt = 1
    while start <= end:
        middle = (start+end)//2
        if middle == key:    # 검색 성공
            return cnt
        elif middle > key:
            end = middle
            cnt += 1
        else:
            start = middle
            cnt += 1

    return False

T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())

    if binarysearch(P, Pa) > binarysearch(P, Pb):
        print(f"#{tc} B")
    elif binarysearch(P, Pa) < binarysearch(P, Pb):
        print(f"#{tc} A")
    else:
        print(f"#{tc} 0")
    
